"""Fix greenlet errors by changing lazy loading strategy

Revision ID: 67b103c1922d
Revises: baa545f90eda
Create Date: 2023-12-29 15:40:37.220978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models import DatabaseModel


# revision identifiers, used by Alembic.
revision: str = '67b103c1922d'
down_revision: Union[str, None] = 'baa545f90eda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###