"""empty message

Revision ID: 083a4cff4055
Revises: 1421289d64f5
Create Date: 2022-04-19 16:42:34.960003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '083a4cff4055'
down_revision = '1421289d64f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('section', sa.Column('assignedInstructor', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'section', 'instructor', ['assignedInstructor'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'section', type_='foreignkey')
    op.drop_column('section', 'assignedInstructor')
    # ### end Alembic commands ###
