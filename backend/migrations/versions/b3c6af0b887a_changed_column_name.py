"""changed column name

Revision ID: b3c6af0b887a
Revises: 73f9fba68150
Create Date: 2023-12-22 12:39:40.429428

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b3c6af0b887a'
down_revision: Union[str, None] = '73f9fba68150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collections')
    op.add_column('images', sa.Column('clothes_set_id', sa.BIGINT(), nullable=True))
    op.drop_constraint('images_collection_id_fkey', 'images', type_='foreignkey')
    op.create_foreign_key(None, 'images', 'clothes_sets', ['clothes_set_id'], ['id'], ondelete='CASCADE')
    op.drop_column('images', 'collection_id')
    op.add_column('items', sa.Column('clothes_set_id', sa.BIGINT(), nullable=True))
    op.drop_constraint('items_collection_id_fkey', 'items', type_='foreignkey')
    op.create_foreign_key(None, 'items', 'clothes_sets', ['clothes_set_id'], ['id'], ondelete='CASCADE')
    op.drop_column('items', 'collection_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('collection_id', sa.BIGINT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.create_foreign_key('items_collection_id_fkey', 'items', 'collections', ['collection_id'], ['id'],
                          ondelete='CASCADE')
    op.drop_column('items', 'clothes_set_id')
    op.add_column('images', sa.Column('collection_id', sa.BIGINT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.create_foreign_key('images_collection_id_fkey', 'images', 'collections', ['collection_id'], ['id'],
                          ondelete='CASCADE')
    op.drop_column('images', 'clothes_set_id')
    op.create_table('collections',
                    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
                    sa.Column('desc', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='collections_pkey')
                    )
    # ### end Alembic commands ###
