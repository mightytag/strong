"""Update Exercise table

Revision ID: 05de8842b6c6
Revises: 9e0b9d3327de
Create Date: 2020-10-16 13:09:58.937818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05de8842b6c6'
down_revision = '9e0b9d3327de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('exercises', 'typeId',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('exercises', 'typeId',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###