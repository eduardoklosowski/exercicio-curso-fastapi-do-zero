"""add coluns created_at and updated_at in todos

Revision ID: a5d0fbdc7fca
Revises: d997786b1504
Create Date: 2024-08-04 15:46:13.952430

"""

from typing import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a5d0fbdc7fca'
down_revision: str | None = 'd997786b1504'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        'todos', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False)
    )
    op.add_column(
        'todos', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('todos', 'updated_at')
    op.drop_column('todos', 'created_at')
