"""empty message

Revision ID: 03201ee89cef
Revises: b91657910e94
Create Date: 2024-10-10 16:28:31.559672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03201ee89cef'
down_revision = 'b91657910e94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)

    # ### end Alembic commands ###
