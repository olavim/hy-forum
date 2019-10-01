"""admin_user

Revision ID: 9f4b6d0a0891
Revises: 2c84352ffc7b
Create Date: 2019-10-01 21:52:42.543312

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from application.models.user import User
from application.models.role import Role

# revision identifiers, used by Alembic.
revision = '9f4b6d0a0891'
down_revision = '2c84352ffc7b'
branch_labels = None
depends_on = None

def upgrade():
    session = Session(bind=op.get_bind())

    # Delete any existing users with name 'admin'
    user = session.query(User).filter_by(username='admin').delete()

    # Admin password is defined with environment variable
    user = User('admin')
    role = session.query(Role).filter_by(name='admin').first()
    user.roles.append(role)
    session.add(user)
    session.commit()

def downgrade():
    session = Session(bind=op.get_bind())
    session.query(User).filter_by(username='admin').delete()
    session.commit()
