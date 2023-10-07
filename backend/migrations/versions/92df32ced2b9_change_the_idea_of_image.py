"""change the idea of Image

Revision ID: 92df32ced2b9
Revises: 8f18537e77e3
Create Date: 2023-10-07 10:37:26.204447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models import DatabaseModel


# revision identifiers, used by Alembic.
revision: str = '92df32ced2b9'
down_revision: Union[str, None] = '8f18537e77e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
