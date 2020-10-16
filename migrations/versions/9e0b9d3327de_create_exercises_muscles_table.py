"""Create Exercises_Muscles table

Revision ID: 9e0b9d3327de
Revises: 56ecf0623038
Create Date: 2020-10-16 12:55:39.143828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e0b9d3327de'
down_revision = '56ecf0623038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises_muscles',
    sa.Column('exerciseId', sa.Integer(), nullable=False),
    sa.Column('muscleId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exerciseId'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['muscleId'], ['muscles.id'], ),
    sa.PrimaryKeyConstraint('exerciseId', 'muscleId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises_muscles')
    # ### end Alembic commands ###
