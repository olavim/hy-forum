"""baseline

Revision ID: 3ef88ca05299
Revises:
Create Date: 2019-09-22 16:07:06.123088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow

# revision identifiers, used by Alembic.
revision = '3ef88ca05299'
down_revision = None
branch_labels = ('baseline',)
depends_on = None


def upgrade():
    op.create_table('topic',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('title', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('username', sa.String(length=255), nullable=True),
        sa.Column('password_hash', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )
    op.create_table('thread',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('title', sa.String(length=255), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('text', sa.Text(), nullable=True),
        sa.Column('thread_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('message')
    op.drop_table('thread')
    op.drop_table('user')
    op.drop_table('topic')
