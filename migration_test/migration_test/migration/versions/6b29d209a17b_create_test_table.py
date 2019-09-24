"""create_test_table

Revision ID: 6b29d209a17b
Revises: 
Create Date: 2019-09-24 16:04:44.004938

"""
from alembic import op

revision = '6b29d209a17b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE test (
            first_column serial primary key,
            second_column varchar,
            third_column varchar
        );
    """)


def downgrade():
    op.execute("DROP TABLE test;")
