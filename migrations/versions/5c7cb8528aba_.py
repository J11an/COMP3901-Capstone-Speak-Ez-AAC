"""empty message

Revision ID: 5c7cb8528aba
Revises: 76f191d2d346
Create Date: 2023-05-09 10:18:04.882158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c7cb8528aba'
down_revision = '76f191d2d346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('word_id')
    )
    op.create_table('pronouns',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pronouns')
    op.drop_table('articles')
    # ### end Alembic commands ###