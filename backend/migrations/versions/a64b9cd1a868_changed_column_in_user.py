"""changed column in user

Revision ID: a64b9cd1a868
Revises: 29d30b487935
Create Date: 2023-10-22 14:13:47.064557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models import DatabaseModel


# revision identifiers, used by Alembic.
revision: str = 'a64b9cd1a868'
down_revision: Union[str, None] = '29d30b487935'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=100), nullable=False))
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
