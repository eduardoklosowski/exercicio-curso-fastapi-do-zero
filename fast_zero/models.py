from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship


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

    todos: Mapped[list['Todo']] = relationship(back_populates='user', cascade='all, delete-orphan', init=False)


class TodoState(str, Enum):
    draft = 'draft'
    todo = 'todo'
    doing = 'doing'
    done = 'done'
    trash = 'trash'


class Todo(TimestampMixin, Base, kw_only=True):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    description: Mapped[str]
    state: Mapped[TodoState]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['User'] = relationship(back_populates='todos', init=False)
