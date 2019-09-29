"""role permissions

Revision ID: e0f4936da1bf
Revises: 97becb89d007
Create Date: 2019-09-29 19:39:16.830514

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow


# revision identifiers, used by Alembic.
revision = 'e0f4936da1bf'
down_revision = '97becb89d007'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role_permission',
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('permission_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )


def downgrade():
    op.drop_table('role_permission')
