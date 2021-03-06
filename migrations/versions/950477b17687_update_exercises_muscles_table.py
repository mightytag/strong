"""Update Exercises_Muscles table

Revision ID: 950477b17687
Revises: bc340c5b4097
Create Date: 2020-10-16 18:28:34.535221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950477b17687'
down_revision = 'bc340c5b4097'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises_muscles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises_muscles',
    sa.Column('exerciseId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('muscleId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['exerciseId'], ['exercises.id'], name='exercises_muscles_exerciseId_fkey'),
    sa.ForeignKeyConstraint(['muscleId'], ['muscles.id'], name='exercises_muscles_muscleId_fkey'),
    sa.PrimaryKeyConstraint('exerciseId', 'muscleId', name='exercises_muscles_pkey')
    )
    # ### end Alembic commands ###
