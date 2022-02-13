"""create post table

Revision ID: 51ef05587758
Revises:
Create Date: 2022-02-13 13:37:32.475701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51ef05587758'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
                    sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
