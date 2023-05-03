"""empty message

Revision ID: 93824eb83184
Revises: e0d7fcc65407
Create Date: 2023-05-02 18:41:46.625281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93824eb83184'
down_revision = 'e0d7fcc65407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partsof_speech', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pos_id', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('pos', sa.String(length=20), nullable=True))
        batch_op.drop_column('partofspeech')
        batch_op.drop_column('partofspeech_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partsof_speech', schema=None) as batch_op:
        batch_op.add_column(sa.Column('partofspeech_id', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('partofspeech', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.drop_column('pos')
        batch_op.drop_column('pos_id')

    # ### end Alembic commands ###
