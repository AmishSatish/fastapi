"""add last few column in posts

Revision ID: a0cb15956e29
Revises: 4031b7ea6b59
Create Date: 2022-02-13 15:20:47.554769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0cb15956e29'
down_revision = '4031b7ea6b59'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("published",
                                    sa.Boolean,nullable=False,
                                    server_default="TRUE"))
    op.add_column("posts",sa.Column("created_at"
                                    ,sa.TIMESTAMP(timezone=True)
                                    ,nullable=False
                                    ,server_default=sa.text("now()")))
    pass


def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
