"""empty message

Revision ID: ebde70f0fbb3
Revises: 
Create Date: 2023-05-02 15:31:27.397994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebde70f0fbb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partsof_speech',
    sa.Column('partofspeech_id', sa.String(length=20), nullable=False),
    sa.Column('partofspeech', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('partofspeech_id')
    )
    op.create_table('symbols',
    sa.Column('symbol_id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('symbol_id')
    )
    op.create_table('adjectives',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.Column('pos_id', sa.String(length=20), nullable=True),
    sa.Column('comparitive', sa.String(length=20), nullable=True),
    sa.Column('superlative', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['pos_id'], ['partsof_speech.partofspeech_id'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    op.create_table('nouns',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.Column('pos_id', sa.String(length=20), nullable=True),
    sa.Column('plural', sa.String(length=20), nullable=True),
    sa.Column('possessive', sa.String(length=20), nullable=True),
    sa.Column('male', sa.String(length=20), nullable=True),
    sa.Column('female', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['pos_id'], ['partsof_speech.partofspeech_id'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    op.create_table('verbs',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.Column('pos_id', sa.String(length=20), nullable=True),
    sa.Column('plural', sa.String(length=20), nullable=True),
    sa.Column('past', sa.String(length=20), nullable=True),
    sa.Column('present_cont', sa.String(length=20), nullable=True),
    sa.Column('future', sa.String(length=20), nullable=True),
    sa.Column('perfect', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['pos_id'], ['partsof_speech.partofspeech_id'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    op.create_table('words',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=20), nullable=True),
    sa.Column('partofspeech', sa.String(length=20), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('sub_category', sa.String(length=20), nullable=True),
    sa.Column('time', sa.String(length=20), nullable=True),
    sa.Column('place', sa.String(length=20), nullable=True),
    sa.Column('symbol_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['partofspeech'], ['partsof_speech.partofspeech_id'], ),
    sa.ForeignKeyConstraint(['symbol_id'], ['symbols.symbol_id'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    op.drop_table('verbs')
    op.drop_table('nouns')
    op.drop_table('adjectives')
    op.drop_table('symbols')
    op.drop_table('partsof_speech')
    # ### end Alembic commands ###