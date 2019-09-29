"""permissions

Revision ID: 97becb89d007
Revises: 193574a7d6be
Create Date: 2019-09-29 19:35:49.717023

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utc.now import utcnow


# revision identifiers, used by Alembic.
revision = '97becb89d007'
down_revision = '193574a7d6be'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('permission',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=utcnow(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=utcnow(), onupdate=utcnow(), nullable=True),
        sa.Column('permission', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('permission')
    )


def downgrade():
    op.drop_table('permission')
