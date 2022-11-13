"""init

Revision ID: 00bd7e2fc3bb
Revises:
Create Date: 2022-11-10 11:13:22.923472

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "00bd7e2fc3bb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("surname", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("phone", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("hashed_password", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("is_stuff", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", "email", name="users_pkey"),
        sa.UniqueConstraint("email", name="users_email_key"),
        sa.UniqueConstraint("id", name="users_id_key"),
    )
    # ### end Alembic commands ###
