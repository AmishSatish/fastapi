"""add content column to posts table

Revision ID: 0e79af8932c4
Revises: 51ef05587758
Create Date: 2022-02-13 13:53:30.845128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e79af8932c4'
down_revision = '51ef05587758'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column("posts","content")
    pass