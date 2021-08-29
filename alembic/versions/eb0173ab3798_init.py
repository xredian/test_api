"""init

Revision ID: eb0173ab3798
Revises: 
Create Date: 2020-12-23 13:31:03.965743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb0173ab3798'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('surname', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('patronymic', sa.String, nullable=False),
        sa.Column('year_of_birth', sa.Integer, nullable=False),
        sa.Column('personnel_number', sa.Integer, unique=True),
        sa.Column('salary', sa.Float, nullable=False),
        sa.Column('position', sa.String, nullable=False),
        sa.Column('legal_entity', sa.String, nullable=False),
        sa.Column('structural_subdivision', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('employees')
