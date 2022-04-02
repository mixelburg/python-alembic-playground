"""users table

Revision ID: 191d10f5d8eb
Revises: 2582c30ce1a5
Create Date: 2022-04-02 16:30:31.270921

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '191d10f5d8eb'
down_revision = '2582c30ce1a5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('users')
