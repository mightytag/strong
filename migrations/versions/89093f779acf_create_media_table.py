"""Create Media table

Revision ID: 89093f779acf
Revises: c84ac1b1af37
Create Date: 2020-10-16 12:45:28.754568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89093f779acf'
down_revision = 'c84ac1b1af37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.Text(), nullable=False),
    sa.Column('typeId', sa.Integer(), nullable=False),
    sa.Column('exerciseId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exerciseId'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['typeId'], ['media_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media')
    # ### end Alembic commands ###
