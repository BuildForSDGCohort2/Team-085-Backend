"""
empty message

Revision ID: 9863320f48e2
Revises: 8fc2f2585db8
Create Date: 2020-08-29 13:31:28.387183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9863320f48e2'
down_revision = '8fc2f2585db8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=200), nullable=False),
    sa.Column('lastname', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artisan_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['artisan_id'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=400), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=400), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_table('Jobs')
    op.drop_table('Users')
    # ### end Alembic commands ###
