"""Revise User

Revision ID: 0c831ce93f8a
Revises: 7b3fa226df2e
Create Date: 2020-10-17 06:17:44.622463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c831ce93f8a'
down_revision = '7b3fa226df2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_firstName_key', 'users', type_='unique')
    op.drop_constraint('users_lastName_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_lastName_key', 'users', ['lastName'])
    op.create_unique_constraint('users_firstName_key', 'users', ['firstName'])
    # ### end Alembic commands ###
