"""add language to posts

Revision ID: 5f4c78884424
Revises: d9d083a0a654
Create Date: 2019-10-26 19:53:54.751717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5f4c78884424"
down_revision = "d9d083a0a654"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("post", sa.Column("language", sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("post", "language")
    # ### end Alembic commands ###