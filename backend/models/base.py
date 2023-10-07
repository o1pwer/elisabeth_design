from __future__ import annotations

import logging
import re
from typing import Optional, Type, cast, Any, Dict, Pattern, Final

from pydantic import BaseModel
from sqlalchemy import inspect, Column, TIMESTAMP, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import registry, has_inherited_table, declared_attr
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()

# Регулярное выражение, которое разделяет строку по заглавным буквам
TABLE_NAME_REGEX: Pattern[str] = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])|(?<=[^A-Z])(?=[A-Z])")
PLURAL: Final[str] = "s"

logger = logging.getLogger(__name__)


class ImmutableProperties(BaseModel):
    properties: dict

    def __getattr__(self, name):
        try:
            return self.properties[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        raise AttributeError("ImmutableProperties object is immutable")

    def __delattr__(self, name):
        raise AttributeError("ImmutableProperties object is immutable")


class DatabaseModel(metaclass=DeclarativeMeta):
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
        Автоматически генерирует имя таблицы из названия модели, примеры:

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
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

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

    def as_dict(self) -> Dict[Any, Any]:
        return self._get_attributes()


class TimedBaseModel(DatabaseModel):
    __abstract__ = True

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                        default=func.now(),
                        onupdate=func.now(),
                        server_default=func.now())
