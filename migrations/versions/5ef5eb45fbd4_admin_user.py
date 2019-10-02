"""admin user

Revision ID: 5ef5eb45fbd4
Revises: 9f4b6d0a0891
Create Date: 2019-10-02 15:14:40.830990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from application.models.user import User
from application.models.role import Role

# revision identifiers, used by Alembic.
revision = '5ef5eb45fbd4'
down_revision = '9f4b6d0a0891'
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
