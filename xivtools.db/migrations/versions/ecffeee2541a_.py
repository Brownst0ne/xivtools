"""empty message

Revision ID: ecffeee2541a
Revises: fd20afbb1aea
Create Date: 2020-02-19 12:56:48.123793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecffeee2541a'
down_revision = 'fd20afbb1aea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('action', sa.Column('actiontimelinehit', sa.Text(), nullable=True))
    op.add_column('action', sa.Column('animationend', sa.Text(), nullable=True))
    op.add_column('action', sa.Column('animationstart', sa.Text(), nullable=True))
    op.add_column('action', sa.Column('unk1', sa.Text(), nullable=True))
    op.add_column('action', sa.Column('unk19', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk20', sa.Text(), nullable=True))
    op.add_column('action', sa.Column('unk22', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk23', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk24', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk26', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk30', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk4', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk40', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk45', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk49', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk50', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk54', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk55', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk56', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk57', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk58', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk59', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk60', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk61', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk62', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('unk63', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk64', sa.Boolean(), nullable=True))
    op.add_column('action', sa.Column('unk9', sa.SMALLINT(), nullable=True))
    op.add_column('action', sa.Column('vfx', sa.Text(), nullable=True))
    op.add_column('item', sa.Column('lot', sa.Boolean(), nullable=True))
    op.add_column('item', sa.Column('unk36', sa.SMALLINT(), nullable=True))
    op.add_column('item', sa.Column('unk41', sa.SMALLINT(), nullable=True))
    op.add_column('item', sa.Column('unk50', sa.SMALLINT(), nullable=True))
    op.add_column('item', sa.Column('unk54', sa.SMALLINT(), nullable=True))
    op.add_column('item', sa.Column('unk89', sa.SMALLINT(), nullable=True))
    op.drop_column('item', 'unk53')
    op.drop_column('item', 'unk88')
    op.drop_column('item', 'unk40')
    op.drop_column('item', 'unk49')
    op.drop_column('item', 'isequippable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('isequippable', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('unk49', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('unk40', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('unk88', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('unk53', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_column('item', 'unk89')
    op.drop_column('item', 'unk54')
    op.drop_column('item', 'unk50')
    op.drop_column('item', 'unk41')
    op.drop_column('item', 'unk36')
    op.drop_column('item', 'lot')
    op.drop_column('action', 'vfx')
    op.drop_column('action', 'unk9')
    op.drop_column('action', 'unk64')
    op.drop_column('action', 'unk63')
    op.drop_column('action', 'unk62')
    op.drop_column('action', 'unk61')
    op.drop_column('action', 'unk60')
    op.drop_column('action', 'unk59')
    op.drop_column('action', 'unk58')
    op.drop_column('action', 'unk57')
    op.drop_column('action', 'unk56')
    op.drop_column('action', 'unk55')
    op.drop_column('action', 'unk54')
    op.drop_column('action', 'unk50')
    op.drop_column('action', 'unk49')
    op.drop_column('action', 'unk45')
    op.drop_column('action', 'unk40')
    op.drop_column('action', 'unk4')
    op.drop_column('action', 'unk30')
    op.drop_column('action', 'unk26')
    op.drop_column('action', 'unk24')
    op.drop_column('action', 'unk23')
    op.drop_column('action', 'unk22')
    op.drop_column('action', 'unk20')
    op.drop_column('action', 'unk19')
    op.drop_column('action', 'unk1')
    op.drop_column('action', 'animationstart')
    op.drop_column('action', 'animationend')
    op.drop_column('action', 'actiontimelinehit')
    # ### end Alembic commands ###
