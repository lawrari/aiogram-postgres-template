"""initial

Revision ID: 3cc4624f2eb6
Revises: 
Create Date: 2023-02-03 16:44:17.479652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc4624f2eb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.BigInteger, unique=True, nullable=False),
        sa.Column('username', sa.String(255), unique=True, nullable=True),
        sa.Column('first_name', sa.String(255), nullable=True),
        sa.Column('last_name', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('role', sa.String(255), nullable=False),
        sa.Column('balance', sa.Integer, nullable=False),
        sa.Column('is_blocked', sa.Boolean, nullable=False),
        sa.Column('invited_by', sa.BigInteger, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('Users')
