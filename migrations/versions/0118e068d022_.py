"""topic description

Revision ID: 0118e068d022
Revises: 3ef88ca05299
Create Date: 2019-09-22 16:17:33.438414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0118e068d022'
down_revision = '3ef88ca05299'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('topic', sa.Column('description', sa.String(length=255), nullable=True))


def downgrade():
    with op.batch_alter_table('topic') as batch_op:
        batch_op.drop_column('description')
