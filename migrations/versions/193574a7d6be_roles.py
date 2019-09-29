"""roles

Revision ID: 193574a7d6be
Revises: 0118e068d022
Create Date: 2019-09-29 19:30:50.982132

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow


# revision identifiers, used by Alembic.
revision = '193574a7d6be'
down_revision = '0118e068d022'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('role')
