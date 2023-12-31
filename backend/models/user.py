from sqlalchemy import Column, text, TIMESTAMP, Integer, VARCHAR

from models.base import DatabaseModel


class User(DatabaseModel):
    """SQLAlchemy model which represents User object."""
    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(60), nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    password = Column(VARCHAR(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
