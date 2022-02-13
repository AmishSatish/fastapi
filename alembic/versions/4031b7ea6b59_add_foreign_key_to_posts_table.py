"""add foreign key to posts table

Revision ID: 4031b7ea6b59
Revises: da6fda457c79
Create Date: 2022-02-13 15:12:06.989828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4031b7ea6b59'
down_revision = 'da6fda457c79'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",source_table="posts",
                          referent_table="users",
                          local_cols=["owner_id"],
                          remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
    pass
