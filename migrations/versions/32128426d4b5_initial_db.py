"""Initial DB

Revision ID: 32128426d4b5
Revises: 
Create Date: 2017-10-27 14:18:04.492166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32128426d4b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('delivered_at', sa.DateTime(), nullable=True),
    sa.Column('dropped_at', sa.DateTime(), nullable=True),
    sa.Column('apikey', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('jobid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sessions'))
    )
    op.create_table('users',
    sa.Column('apikey', sa.String(), nullable=False),
    sa.Column('projectname', sa.String(), nullable=True),
    sa.Column('jobname', sa.String(), nullable=True),
    sa.Column('createdat', sa.DateTime(), nullable=True),
    sa.Column('limitnodes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('apikey', name=op.f('pk_users'))
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('chassis', sa.String(), nullable=True),
    sa.Column('used_count', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('distro', sa.String(), nullable=True),
    sa.Column('rel', sa.String(), nullable=True),
    sa.Column('ver', sa.String(), nullable=True),
    sa.Column('arch', sa.String(), nullable=True),
    sa.Column('pool', sa.Integer(), nullable=True),
    sa.Column('console_port', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], name=op.f('fk_stock_session_id_sessions')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_stock'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    op.drop_table('users')
    op.drop_table('sessions')
    # ### end Alembic commands ###