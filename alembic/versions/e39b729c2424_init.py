"""init

Revision ID: e39b729c2424
Revises: 
Create Date: 2022-01-06 17:52:32.078365

"""
from typing import Optional
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e39b729c2424'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'matrix',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('problem_statement', sa.String, nullable=False)
    )

def downgrade():
    op.drop_table('matrix')
