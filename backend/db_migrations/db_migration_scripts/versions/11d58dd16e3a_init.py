"""init

Revision ID: 11d58dd16e3a
Revises: 
Create Date: 2024-11-04 18:40:41.209179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '11d58dd16e3a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usssersss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usssersss_email'), 'usssersss', ['email'], unique=True)
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['usssersss.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    op.drop_index(op.f('ix_usssersss_email'), table_name='usssersss')
    op.drop_table('usssersss')
    # ### end Alembic commands ###
