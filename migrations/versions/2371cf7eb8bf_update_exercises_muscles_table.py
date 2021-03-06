"""Update Exercises_Muscles table

Revision ID: 2371cf7eb8bf
Revises: 950477b17687
Create Date: 2020-10-16 18:29:07.621590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2371cf7eb8bf'
down_revision = '950477b17687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises_muscles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exerciseId', sa.Integer(), nullable=False),
    sa.Column('muscleId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exerciseId'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['muscleId'], ['muscles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises_muscles')
    # ### end Alembic commands ###
