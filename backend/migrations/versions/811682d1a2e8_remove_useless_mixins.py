"""remove useless mixins

Revision ID: 811682d1a2e8
Revises: a64b9cd1a868
Create Date: 2023-12-03 16:38:14.193751

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '811682d1a2e8'
down_revision: Union[str, None] = 'a64b9cd1a868'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
