"""alter test table

Revision ID: 0b08e00b111f
Revises: 6b29d209a17b
Create Date: 2019-09-24 18:10:12.564545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b08e00b111f'
down_revision = '6b29d209a17b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""ALTER TABLE test ADD COLUMN fourth_column varchar;""")


def downgrade():
    op.execute("""ALTER TABLE test DROP COLUMN fourth_column""")
