from sqlalchemy import BIGINT, Column, VARCHAR, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from models import DatabaseModel


class Item(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    collection_id = Column(ForeignKey("collections.id", ondelete="CASCADE"))
    images = relationship("Image", backref="item")


class Collection(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    items = relationship("Item", backref="collection")
    images = relationship("Image", backref="collection")


class Image(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    content = Column(LargeBinary, nullable=False)
    collection_id = Column(ForeignKey("collections.id", ondelete="CASCADE"))
    item_id = Column(ForeignKey("items.id", ondelete="CASCADE"))
