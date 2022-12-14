"""Add Tutorial model

Revision ID: ed3d77797231
Revises: 
Create Date: 2022-08-27 19:26:44.810874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed3d77797231'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('a',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('create_date', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('b',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_id', sa.Integer(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['a_id'], ['a.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('b')
    op.drop_table('a')
    # ### end Alembic commands ###
