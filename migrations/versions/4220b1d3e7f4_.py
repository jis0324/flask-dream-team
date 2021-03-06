"""empty message

Revision ID: 4220b1d3e7f4
Revises: 06f244b6afc9
Create Date: 2020-12-18 09:49:24.333903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4220b1d3e7f4'
down_revision = '06f244b6afc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('taskheader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('taskheader')
    # ### end Alembic commands ###
