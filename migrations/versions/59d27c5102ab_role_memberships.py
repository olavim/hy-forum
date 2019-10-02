"""role memberships

Revision ID: 59d27c5102ab
Revises: e0f4936da1bf
Create Date: 2019-09-29 19:42:02.023096

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow


# revision identifiers, used by Alembic.
revision = '59d27c5102ab'
down_revision = 'e0f4936da1bf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role_membership',
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('role_id', 'user_id')
    )

def downgrade():
    op.drop_table('role_membership')
