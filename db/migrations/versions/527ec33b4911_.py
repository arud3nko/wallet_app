"""empty message

Revision ID: 527ec33b4911
Revises: 1cba7239296e
Create Date: 2024-06-16 21:25:43.039179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '527ec33b4911'
down_revision: Union[str, None] = '1cba7239296e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('passcode', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'passcode')
    # ### end Alembic commands ###
