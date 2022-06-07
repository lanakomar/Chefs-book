"""modified recipe table

Revision ID: 6abdc6b8e28d
Revises: 85c41b305e7f
Create Date: 2022-06-07 14:20:36.630794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6abdc6b8e28d'
down_revision = '85c41b305e7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('servings', sa.Integer(), nullable=False))
    op.drop_column('recipes', 'date_created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('date_created', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_column('recipes', 'servings')
    # ### end Alembic commands ###