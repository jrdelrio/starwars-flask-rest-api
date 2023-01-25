"""empty message

Revision ID: 6020586d2ebc
Revises: f30ecc0c88c3
Create Date: 2023-01-23 15:58:52.890350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6020586d2ebc'
down_revision = 'f30ecc0c88c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###