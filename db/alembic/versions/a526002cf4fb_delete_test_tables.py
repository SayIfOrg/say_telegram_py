"""delete test tables

Revision ID: a526002cf4fb
Revises: a4ab8a2a7feb
Create Date: 2022-08-29 22:33:53.145513

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a526002cf4fb'
down_revision = 'a4ab8a2a7feb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('b')
    op.drop_table('a')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('a',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('a_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('data', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('create_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='a_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('b',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('a_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('data', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['a_id'], ['a.id'], name='b_a_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='b_pkey')
    )
    # ### end Alembic commands ###
