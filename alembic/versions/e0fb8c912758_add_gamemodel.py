"""Add GameModel

Revision ID: e0fb8c912758
Revises: 
Create Date: 2023-03-04 19:24:14.714777

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0fb8c912758'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_session',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chat_id')
    )
    op.create_table('game',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('users', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('state_photo', sa.Boolean(), nullable=True),
    sa.Column('state_in_game', sa.Boolean(), nullable=True),
    sa.Column('state_wait_votes', sa.Boolean(), nullable=True),
    sa.Column('new_pair', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('first_votes', sa.BigInteger(), nullable=True),
    sa.Column('second_votes', sa.BigInteger(), nullable=True),
    sa.Column('state_send_photo', sa.Boolean(), nullable=True),
    sa.Column('voters', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('amount_users', sa.BigInteger(), nullable=True),
    sa.Column('last_winner', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['game_session.chat_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participants',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('wins', sa.BigInteger(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('owner_id', sa.BigInteger(), nullable=True),
    sa.Column('photo_id', sa.BigInteger(), nullable=True),
    sa.Column('access_key', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['game_session.chat_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participants')
    op.drop_table('game')
    op.drop_table('game_session')
    # ### end Alembic commands ###
