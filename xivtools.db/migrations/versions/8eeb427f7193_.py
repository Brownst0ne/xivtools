"""empty message

Revision ID: 8eeb427f7193
Revises: 69740e583675
Create Date: 2020-01-21 18:47:40.509756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eeb427f7193'
down_revision = '69740e583675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('singular', sa.Text(), nullable=True),
    sa.Column('adjective', sa.Integer(), nullable=True),
    sa.Column('plural', sa.Text(), nullable=True),
    sa.Column('possessivepronoun', sa.SMALLINT(), nullable=True),
    sa.Column('startswithvowel', sa.SMALLINT(), nullable=True),
    sa.Column('unk5', sa.SMALLINT(), nullable=True),
    sa.Column('pronoun', sa.SMALLINT(), nullable=True),
    sa.Column('article', sa.SMALLINT(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('icon', sa.Text(), nullable=True),
    sa.Column('levelitem', sa.SMALLINT(), nullable=True),
    sa.Column('rarity', sa.SMALLINT(), nullable=True),
    sa.Column('filtergroup', sa.SMALLINT(), nullable=True),
    sa.Column('additionaldata', sa.Text(), nullable=True),
    sa.Column('itemuicategory', sa.Text(), nullable=True),
    sa.Column('itemsearchcategory', sa.Text(), nullable=True),
    sa.Column('equipslotcategory', sa.SMALLINT(), nullable=True),
    sa.Column('unk18', sa.Integer(), nullable=True),
    sa.Column('stacksize', sa.Integer(), nullable=True),
    sa.Column('isunique', sa.Boolean(), nullable=True),
    sa.Column('isuntradable', sa.Boolean(), nullable=True),
    sa.Column('isindisposable', sa.Boolean(), nullable=True),
    sa.Column('isequippable', sa.Boolean(), nullable=True),
    sa.Column('pricemid', sa.Integer(), nullable=True),
    sa.Column('pricelow', sa.Integer(), nullable=True),
    sa.Column('canbehq', sa.Boolean(), nullable=True),
    sa.Column('isdyeable', sa.Boolean(), nullable=True),
    sa.Column('iscrestworthy', sa.Boolean(), nullable=True),
    sa.Column('itemaction', sa.SMALLINT(), nullable=True),
    sa.Column('unk30', sa.SMALLINT(), nullable=True),
    sa.Column('cooldowns', sa.SMALLINT(), nullable=True),
    sa.Column('classjobrepair', sa.Text(), nullable=True),
    sa.Column('itemrepair', sa.Text(), nullable=True),
    sa.Column('itemglamour', sa.Text(), nullable=True),
    sa.Column('salvage', sa.SMALLINT(), nullable=True),
    sa.Column('iscollectable', sa.Boolean(), nullable=True),
    sa.Column('alwayscollectable', sa.Boolean(), nullable=True),
    sa.Column('aetherialreduce', sa.SMALLINT(), nullable=True),
    sa.Column('levelequip', sa.SMALLINT(), nullable=True),
    sa.Column('unk40', sa.SMALLINT(), nullable=True),
    sa.Column('equiprestriction', sa.SMALLINT(), nullable=True),
    sa.Column('classjobcategory', sa.Text(), nullable=True),
    sa.Column('grandcompany', sa.Text(), nullable=True),
    sa.Column('itemseries', sa.Text(), nullable=True),
    sa.Column('baseparammodifier', sa.SMALLINT(), nullable=True),
    sa.Column('modelmain', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('modelsub', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('classjobuse', sa.Text(), nullable=True),
    sa.Column('unk49', sa.SMALLINT(), nullable=True),
    sa.Column('damagephys', sa.SMALLINT(), nullable=True),
    sa.Column('damagemag', sa.SMALLINT(), nullable=True),
    sa.Column('delayms', sa.SMALLINT(), nullable=True),
    sa.Column('unk53', sa.SMALLINT(), nullable=True),
    sa.Column('blockrate', sa.SMALLINT(), nullable=True),
    sa.Column('block', sa.SMALLINT(), nullable=True),
    sa.Column('defensephys', sa.SMALLINT(), nullable=True),
    sa.Column('defensemag', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam0', sa.Text(), nullable=True),
    sa.Column('baseparamvalue0', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam1', sa.Text(), nullable=True),
    sa.Column('baseparamvalue1', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam2', sa.Text(), nullable=True),
    sa.Column('baseparamvalue2', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam3', sa.Text(), nullable=True),
    sa.Column('baseparamvalue3', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam4', sa.Text(), nullable=True),
    sa.Column('baseparamvalue4', sa.SMALLINT(), nullable=True),
    sa.Column('baseparam5', sa.Text(), nullable=True),
    sa.Column('baseparamvalue5', sa.SMALLINT(), nullable=True),
    sa.Column('itemspecialbonus', sa.Text(), nullable=True),
    sa.Column('itemspecialbonusparam', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial0', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial0', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial1', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial1', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial2', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial2', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial3', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial3', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial4', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial4', sa.SMALLINT(), nullable=True),
    sa.Column('baseparamspecial5', sa.Text(), nullable=True),
    sa.Column('baseparamvaluespecial5', sa.SMALLINT(), nullable=True),
    sa.Column('materializetype', sa.SMALLINT(), nullable=True),
    sa.Column('materiaslotcount', sa.SMALLINT(), nullable=True),
    sa.Column('isadvancedmeldingpermitted', sa.Boolean(), nullable=True),
    sa.Column('ispvp', sa.Boolean(), nullable=True),
    sa.Column('unk88', sa.SMALLINT(), nullable=True),
    sa.Column('isglamourous', sa.Boolean(), nullable=True),
    sa.Column('iscraftable', sa.Boolean(), nullable=True),
    sa.Column('craftid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipelookup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unk0', sa.Integer(), nullable=True),
    sa.Column('unk1', sa.Integer(), nullable=True),
    sa.Column('unk2', sa.Integer(), nullable=True),
    sa.Column('unk3', sa.Integer(), nullable=True),
    sa.Column('unk4', sa.Integer(), nullable=True),
    sa.Column('unk5', sa.Integer(), nullable=True),
    sa.Column('unk6', sa.Integer(), nullable=True),
    sa.Column('unk7', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipelookup')
    op.drop_table('item')
    # ### end Alembic commands ###
