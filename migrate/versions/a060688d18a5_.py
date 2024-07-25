"""add updated_at column

Revision ID: a060688d18a5
Revises: a539c6ed914b
Create Date: 2024-07-25 01:49:23.606706

"""

from typing import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a060688d18a5'
down_revision: str | None = 'a539c6ed914b'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        'users', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('users', 'updated_at')
