"""empty message

Revision ID: 69740e583675
Revises: ca4640439833
Create Date: 2020-01-20 17:10:23.309718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69740e583675'
down_revision = 'ca4640439833'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('crafttype', sa.Text(), nullable=True),
    sa.Column('recipeleveltable', sa.SMALLINT(), nullable=True),
    sa.Column('itemresult', sa.Text(), nullable=True),
    sa.Column('amountresult', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient0', sa.Text(), nullable=True),
    sa.Column('amountingredient0', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient1', sa.Text(), nullable=True),
    sa.Column('amountingredient1', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient2', sa.Text(), nullable=True),
    sa.Column('amountingredient2', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient3', sa.Text(), nullable=True),
    sa.Column('amountingredient3', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient4', sa.Text(), nullable=True),
    sa.Column('amountingredient4', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient5', sa.Text(), nullable=True),
    sa.Column('amountingredient5', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient6', sa.Text(), nullable=True),
    sa.Column('amountingredient6', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient7', sa.Text(), nullable=True),
    sa.Column('amountingredient7', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient8', sa.Text(), nullable=True),
    sa.Column('amountingredient8', sa.SMALLINT(), nullable=True),
    sa.Column('itemingredient9', sa.Text(), nullable=True),
    sa.Column('amountingredient9', sa.SMALLINT(), nullable=True),
    sa.Column('unk25', sa.SMALLINT(), nullable=True),
    sa.Column('issecondary', sa.Boolean(), nullable=True),
    sa.Column('materialqualityfactor', sa.SMALLINT(), nullable=True),
    sa.Column('difficultyfactor', sa.SMALLINT(), nullable=True),
    sa.Column('qualityfactor', sa.SMALLINT(), nullable=True),
    sa.Column('durabilityfactor', sa.SMALLINT(), nullable=True),
    sa.Column('unk31', sa.SMALLINT(), nullable=True),
    sa.Column('requiredcraftsmanship', sa.SMALLINT(), nullable=True),
    sa.Column('requiredcontrol', sa.SMALLINT(), nullable=True),
    sa.Column('quicksynthcraftsmanship', sa.SMALLINT(), nullable=True),
    sa.Column('quicksynthcontrol', sa.SMALLINT(), nullable=True),
    sa.Column('secretrecipebook', sa.Text(), nullable=True),
    sa.Column('canquicksynth', sa.Boolean(), nullable=True),
    sa.Column('canhq', sa.Boolean(), nullable=True),
    sa.Column('exprewarded', sa.Boolean(), nullable=True),
    sa.Column('statusrequired', sa.Text(), nullable=True),
    sa.Column('itemrequired', sa.Text(), nullable=True),
    sa.Column('isspecializationrequired', sa.Boolean(), nullable=True),
    sa.Column('unk43', sa.Boolean(), nullable=True),
    sa.Column('patchnumber', sa.SMALLINT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe')
    # ### end Alembic commands ###
