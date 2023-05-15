"""empty message

Revision ID: e3954bffe818
Revises: a84df409e6a1
Create Date: 2023-05-14 20:56:12.735704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3954bffe818'
down_revision = 'a84df409e6a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_phrases', schema=None) as batch_op:
        batch_op.alter_column('saved_phrases',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('category',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.create_unique_constraint('uq_saved_phrases_category', ['saved_phrases', 'category'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_phrases', schema=None) as batch_op:
        batch_op.drop_constraint('uq_saved_phrases_category', type_='unique')
        batch_op.alter_column('category',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('saved_phrases',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###