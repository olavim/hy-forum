"""thread read

Revision ID: a80c1d08132d
Revises: 5ef5eb45fbd4
Create Date: 2019-10-13 00:02:46.680434

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow

# revision identifiers, used by Alembic.
revision = 'a80c1d08132d'
down_revision = '5ef5eb45fbd4'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('thread_read',
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('thread_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('thread_id', 'user_id')
    )

def downgrade():
    op.drop_table('thread_read')
