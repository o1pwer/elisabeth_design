from sqlalchemy import BIGINT, Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from models.base import DatabaseModel


class Item(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    clothes_set_id = Column(ForeignKey("clothes_sets.id", ondelete="CASCADE"))
    images = relationship("Image", backref="item")


class ClothesSet(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    items = relationship("Item", backref="clothes_set")
    images = relationship("Image", backref="clothes_set")


class Image(DatabaseModel):
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    link = Column(VARCHAR(200), nullable=False)
    clothes_set_id = Column(ForeignKey("clothes_sets.id", ondelete="CASCADE"))
    item_id = Column(ForeignKey("items.id", ondelete="CASCADE"))
