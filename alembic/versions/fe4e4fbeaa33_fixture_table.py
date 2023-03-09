"""fixture_table

Revision ID: fe4e4fbeaa33
Revises: c87aaaac1243
Create Date: 2023-02-23 20:23:25.777742

"""
from alembic import op

from datetime import datetime
from models.user_model import User
from models.url_model import Url

# revision identifiers, used by Alembic.
revision = 'fe4e4fbeaa33'
down_revision = 'c87aaaac1243'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.bulk_insert(User.__table__, userInitData)
    op.bulk_insert(Url.__table__, urlInitData)

def downgrade() -> None:
    op.execute("DELETE FROM urls")
    op.execute("DELETE FROM users")


userInitData = [
    {'name': 'Oleg', 'created_at': datetime.now()},
    {'name': 'Vika', 'created_at': datetime.now()},
]

urlInitData = [
    {'value': 'https://alembic.sqlalchemy.org/en/latest/index.html', 'created_at': datetime.now(), 'created_by': 1, 'deleted_at': None, 'deleted_by': None},
    {'value': 'https://fastapi.tiangolo.com/', 'created_at': datetime.now(), 'created_by': 1, 'deleted_at': None, 'deleted_by': None},
    {'value': 'https://docs.pydantic.dev/', 'created_at': datetime.now(), 'created_by': 1, 'deleted_at': None, 'deleted_by': None},
    {'value': 'https://fastapi.tiangolo.com/tutorial/sql-databases/', 'created_at': datetime.now(), 'created_by': 2, 'deleted_at': None, 'deleted_by': None},
    {'value': 'https://alembic.sqlalchemy.org/en/latest/tutorial.html', 'created_at': datetime.now(), 'created_by': 2, 'deleted_at': None, 'deleted_by': None},
    {'value': 'https://www.sqlalchemy.org/', 'created_at': datetime.now(), 'created_by': 2, 'deleted_at': None, 'deleted_by': None},
]
