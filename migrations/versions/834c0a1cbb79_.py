"""empty message

Revision ID: 834c0a1cbb79
Revises: bfec9facf8fd
Create Date: 2024-06-06 20:19:28.462087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '834c0a1cbb79'
down_revision = 'bfec9facf8fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###