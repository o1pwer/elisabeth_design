from sqlalchemy import BIGINT, Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from models.base import DatabaseModel


class Item(DatabaseModel):
    """SQLAlchemy model which represents Item object."""
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    clothes_set_id = Column(ForeignKey("clothes_sets.id", ondelete="CASCADE"))
    images = relationship("Image", backref="item", lazy='joined')


class ClothesSet(DatabaseModel):
    """SQLAlchemy model which represents Clothes set object."""
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    desc = Column(VARCHAR(200), nullable=False)
    items = relationship("Item", backref="clothes_set", lazy='joined')
    images = relationship("Image", backref="clothes_set", lazy='joined')


class Image(DatabaseModel):
    """SQLAlchemy model which represents Image object."""
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    link = Column(VARCHAR(200), nullable=False)
    clothes_set_id = Column(ForeignKey("clothes_sets.id", ondelete="CASCADE"))
    item_id = Column(ForeignKey("items.id", ondelete="CASCADE"))
