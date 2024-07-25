from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(DeclarativeBase, MappedAsDataclass): ...


class TimestampMixin(MappedAsDataclass):
    created_at: Mapped[datetime] = mapped_column(init=False, repr=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, repr=False, server_default=func.now(), onupdate=func.now()
    )


class User(TimestampMixin, Base, kw_only=True):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
