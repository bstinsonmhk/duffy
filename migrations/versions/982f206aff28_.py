"""Directly link sessions to hosts

Revision ID: 982f206aff28
Revises: 0dbead04ed33
Create Date: 2017-10-26 15:25:26.290698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '982f206aff28'
down_revision = '0dbead04ed33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_hosts')
    op.add_column('stock', sa.Column('session_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stock', 'sessions', ['session_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.drop_column('stock', 'session_id')
    op.create_table('session_hosts',
    sa.Column('ssid', sa.VARCHAR(), nullable=True),
    sa.Column('hostname', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['hostname'], [u'stock.hostname'], ),
    sa.ForeignKeyConstraint(['ssid'], [u'sessions.id'], )
    )
    # ### end Alembic commands ###