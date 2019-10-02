"""foreign key fix

Revision ID: 9f4b6d0a0891
Revises: 2c84352ffc7b
Create Date: 2019-10-01 21:52:42.543312

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9f4b6d0a0891'
down_revision = '2c84352ffc7b'
branch_labels = None
depends_on = None

naming_convention = {'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'}

def upgrade():
    with op.batch_alter_table('message', naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_message_thread_id_thread', type_='foreignkey')
        batch_op.drop_constraint('fk_message_user_id_user', type_='foreignkey')

    with op.batch_alter_table('thread', naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_thread_topic_id_topic', type_='foreignkey')
        batch_op.drop_constraint('fk_thread_user_id_user', type_='foreignkey')

    with op.batch_alter_table('thread') as batch_op:
        batch_op.create_foreign_key('fk_thread_topic_id_topic', 'topic', ['topic_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('fk_thread_user_id_user', 'user', ['user_id'], ['id'], ondelete='SET NULL')

    with op.batch_alter_table('message') as batch_op:
        batch_op.create_foreign_key('fk_message_thread_id_thread', 'thread', ['thread_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('fk_message_user_id_user', 'user', ['user_id'], ['id'], ondelete='SET NULL')

def downgrade():
    with op.batch_alter_table('message', naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_message_thread_id_thread')
        batch_op.drop_constraint('fk_message_user_id_user')

    with op.batch_alter_table('thread', naming_convention=naming_convention) as batch_op:
        batch_op.drop_constraint('fk_thread_topic_id_topic')
        batch_op.drop_constraint('fk_thread_user_id_user')

    with op.batch_alter_table('thread') as batch_op:
        batch_op.create_foreign_key('fk_thread_topic_id_topic', 'topic', ['topic_id'], ['id'])
        batch_op.create_foreign_key('fk_thread_user_id_user', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('message') as batch_op:
        batch_op.create_foreign_key('fk_message_thread_id_thread', 'thread', ['thread_id'], ['id'])
        batch_op.create_foreign_key('fk_message_user_id_user', 'user', ['user_id'], ['id'])
