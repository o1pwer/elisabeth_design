from __future__ import annotations

import logging
import re
from typing import Optional, Type, cast, Any, Dict, Pattern, Final

from pydantic import BaseModel
from sqlalchemy import inspect, Column, TIMESTAMP, func
from sqlalchemy.orm import registry, has_inherited_table, declared_attr, class_mapper
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()

# Regex which splits the string by capital letters
TABLE_NAME_REGEX: Pattern[str] = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])|(?<=[^A-Z])(?=[A-Z])")
PLURAL: Final[str] = "s"

logger = logging.getLogger(__name__)


class ImmutableProperties(BaseModel):
    """A class containing "properties" dict, which is immutable."""
    properties: dict

    def __getattr__(self, name):
        try:
            return self.properties[name]
        except KeyError as exc:
            raise AttributeError(name) from exc

    def __setattr__(self, name, value):
        raise AttributeError("ImmutableProperties object is immutable")

    def __delattr__(self, name):
        raise AttributeError("ImmutableProperties object is immutable")


class DatabaseModel(metaclass=DeclarativeMeta):
    """A base class from which all custom models should inherit."""
    __abstract__ = True
    __mapper_args__ = {"eager_defaults": True}

    # noinspection PyUnusedLocal
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    registry = mapper_registry
    metadata = mapper_registry.metadata

    @declared_attr
    def __tablename__(self) -> Optional[str]:
        """
        Auto generates table name from class name.

        OrderItem -> order_items
        Order -> orders
        """
        if has_inherited_table(cast(Type[DatabaseModel], self)):
            return None
        cls_name = cast(Type[DatabaseModel], self).__qualname__
        table_name_parts = re.split(TABLE_NAME_REGEX, cls_name)
        formatted_table_name = "".join(
            f"{table_name_part.lower()}_" for table_name_part in table_name_parts
        )
        last_underscore = formatted_table_name.rfind("_")
        return formatted_table_name[:last_underscore] + PLURAL

    def _get_attributes(self) -> Dict[Any, Any]:
        """Retrieve attribute names for this model, excluding internal attributes and relationships."""
        columns = [column.key for column in class_mapper(self.__class__).columns]
        return {key: getattr(self, key) for key in columns if not key.startswith("_")}

    def __str__(self) -> str:
        attributes = "|".join(str(v) for k, v in self._get_attributes().items())
        return f"{self.__class__.__qualname__} {attributes}"

    def __repr__(self) -> str:
        table_attrs = cast(ImmutableProperties, inspect(self).attrs)
        primary_keys = " ".join(
            f"{key.name}={table_attrs[key.name].value}"
            for key in inspect(self.__class__).primary_key
        )
        return f"{self.__class__.__qualname__}->{primary_keys}"

    async def as_dict(self, visited=None):
        """Returns database object as dictionary, including relationships."""
        if visited is None:
            visited = set()

        obj_id = (self.__class__, self.id)
        if obj_id in visited:
            return {'id': self.id}  # or whatever minimal reference you want

        visited.add(obj_id)
        serialized_data = {}
        for attribute in inspect(self).mapper.column_attrs:
            serialized_data[attribute.key] = getattr(self, attribute.key)

        for relationship in inspect(self).mapper.relationships:
            value = getattr(self, relationship.key)
            if isinstance(value, list):
                serialized_data[relationship.key] = [await item.as_dict(visited) for item in value]
            elif value:
                serialized_data[relationship.key] = await value.as_dict(visited)
            else:
                serialized_data[relationship.key] = None

        return serialized_data

class TimedBaseModel(DatabaseModel):
    """DatabaseModel, but with few additional fields containing dates of creation and last update of the row"""
    __abstract__ = True

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                        default=func.now(),
                        onupdate=func.now(),
                        server_default=func.now())
