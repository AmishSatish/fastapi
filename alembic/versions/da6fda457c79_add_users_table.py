"""add users table

Revision ID: da6fda457c79
Revises: 0e79af8932c4
Create Date: 2022-02-13 14:07:49.495450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da6fda457c79'
down_revision = '0e79af8932c4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,
                              server_default=sa.text("now()")),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
