"""empty message

Revision ID: dadec3d6230a
Revises: 8a60cf7d738c
Create Date: 2020-02-12 15:44:34.235426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dadec3d6230a'
down_revision = '8a60cf7d738c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('raidid', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('raidname', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('pwhash', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdata')
    # ### end Alembic commands ###
