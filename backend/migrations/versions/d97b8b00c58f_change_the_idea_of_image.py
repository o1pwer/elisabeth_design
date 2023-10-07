"""change the idea of Image

Revision ID: d97b8b00c58f
Revises: 92df32ced2b9
Create Date: 2023-10-07 10:41:00.477623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models import DatabaseModel


# revision identifiers, used by Alembic.
revision: str = 'd97b8b00c58f'
down_revision: Union[str, None] = '92df32ced2b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
