"""empty message

Revision ID: 5ef8b3bb369a
Revises: e8bbd0e88b73
Create Date: 2020-09-03 08:13:48.258519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ef8b3bb369a'
down_revision = 'e8bbd0e88b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('join_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'join_date')
    # ### end Alembic commands ###
