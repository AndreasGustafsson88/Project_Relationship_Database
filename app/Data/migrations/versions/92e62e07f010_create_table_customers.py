"""create table customers

Revision ID: 92e62e07f010
Revises: 12dcc8131f1b
Create Date: 2020-11-17 15:07:02.294975

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '92e62e07f010'
down_revision = '12dcc8131f1b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('customer_id', sa.Integer, primary_key=True),
        sa.Column('customer_type', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('customers')
