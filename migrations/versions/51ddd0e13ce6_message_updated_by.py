"""message_updated_by

Revision ID: 51ddd0e13ce6
Revises: a80c1d08132d
Create Date: 2019-10-13 13:21:13.906596

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '51ddd0e13ce6'
down_revision = 'a80c1d08132d'
branch_labels = None
depends_on = None

naming_convention = {'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'}

def upgrade():
    op.add_column('message', sa.Column('updated_by_id', sa.Integer(), nullable=True))

    with op.batch_alter_table('message') as batch_op:
        batch_op.create_foreign_key('fk_message_updated_by_id_user', 'user', ['updated_by_id'], ['id'], ondelete='SET NULL')

def downgrade():
    with op.batch_alter_table('message', naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_message_updated_by_id_user')

    with op.batch_alter_table('message') as batch_op:
        batch_op.drop_column('updated_by_id')
