"""test1 test2

Revision ID: a0ec1a962133
Revises: 07e9950d3749, eff1b556ff52
Create Date: 2022-08-20 01:14:24.190540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ec1a962133'
down_revision = ('07e9950d3749', 'eff1b556ff52')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
