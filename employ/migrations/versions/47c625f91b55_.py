"""empty message

Revision ID: 47c625f91b55
Revises: 
Create Date: 2019-03-20 15:41:36.020763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c625f91b55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('is_enable', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('website', sa.String(length=256), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('logo', sa.String(length=128), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('finance_stage', sa.String(length=16), nullable=True),
    sa.Column('field', sa.String(length=16), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_company_is_enable'), 'company', ['is_enable'], unique=False)
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('is_enable', sa.Boolean(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=8), nullable=False),
    sa.Column('resume', sa.String(length=128), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_is_enable'), 'user', ['is_enable'], unique=False)
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('salary_min', sa.SmallInteger(), nullable=False),
    sa.Column('salary_max', sa.SmallInteger(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('treatment', sa.Text(), nullable=True),
    sa.Column('exp', sa.String(length=16), nullable=True),
    sa.Column('education', sa.String(length=16), nullable=True),
    sa.Column('city', sa.String(length=8), nullable=True),
    sa.Column('tags', sa.String(length=64), nullable=True),
    sa.Column('is_enable', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_job_city'), 'job', ['city'], unique=False)
    op.create_index(op.f('ix_job_education'), 'job', ['education'], unique=False)
    op.create_index(op.f('ix_job_exp'), 'job', ['exp'], unique=False)
    op.create_index(op.f('ix_job_is_enable'), 'job', ['is_enable'], unique=False)
    op.create_index(op.f('ix_job_salary_max'), 'job', ['salary_max'], unique=False)
    op.create_index(op.f('ix_job_salary_min'), 'job', ['salary_min'], unique=False)
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('resume', sa.String(length=128), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('company_response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_delivery_status'), 'delivery', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_delivery_status'), table_name='delivery')
    op.drop_table('delivery')
    op.drop_index(op.f('ix_job_salary_min'), table_name='job')
    op.drop_index(op.f('ix_job_salary_max'), table_name='job')
    op.drop_index(op.f('ix_job_is_enable'), table_name='job')
    op.drop_index(op.f('ix_job_exp'), table_name='job')
    op.drop_index(op.f('ix_job_education'), table_name='job')
    op.drop_index(op.f('ix_job_city'), table_name='job')
    op.drop_table('job')
    op.drop_index(op.f('ix_user_is_enable'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_company_is_enable'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###