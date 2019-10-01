"""initial permissions

Revision ID: 2c84352ffc7b
Revises: 59d27c5102ab
Create Date: 2019-09-29 19:53:57.933126

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from application.models.role import Permission

# revision identifiers, used by Alembic.
revision = '2c84352ffc7b'
down_revision = '59d27c5102ab'
branch_labels = None
depends_on = None

# Users always have some of these permissions when they own the resource in question
permissions = [
    'roles:manage',
    'topics:create',
    'topics:edit',
    'topics:delete',
    'threads:edit',
    'threads:delete',
    'messages:edit',
    'messages:delete'
]

def upgrade():
    session = Session(bind=op.get_bind())

    for permission in permissions:
        item = Permission(permission=permission)
        session.add(item)

    session.commit()

def downgrade():
    session = Session(bind=op.get_bind())

    for permission in permissions:
        session.query(Permission).filter_by(permission=permission).delete()

    session.commit()
