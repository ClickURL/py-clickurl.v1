"""url_table

Revision ID: c87aaaac1243
Revises: d8314c4d9cc2
Create Date: 2023-02-23 20:22:52.963434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87aaaac1243'
down_revision = 'd8314c4d9cc2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('urls',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['deleted_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_id'), 'urls', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_urls_id'), table_name='urls')
    op.drop_table('urls')
