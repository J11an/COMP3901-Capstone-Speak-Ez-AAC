"""empty message

Revision ID: 29ab8782ebd0
Revises: 93824eb83184
Create Date: 2023-05-02 18:53:43.160519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ab8782ebd0'
down_revision = '93824eb83184'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adjectives', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comparative', sa.String(length=20), nullable=True))
        batch_op.drop_column('comparitive')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adjectives', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comparitive', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.drop_column('comparative')

    # ### end Alembic commands ###