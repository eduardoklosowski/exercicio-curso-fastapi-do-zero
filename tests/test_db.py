from unittest.mock import patch

import pytest
from fast_zero.database import get_session
from fast_zero.models import User
from sqlalchemy import create_engine, select, text


@patch('fast_zero.database.engine', create_engine('sqlite:///:memory:'))
def test_get_session():
    ret = get_session()
    session = next(ret)

    result = session.execute(text('SELECT 1 + 1')).one()

    session.close()
    with pytest.raises(StopIteration):
        next(ret)

    assert result == (2,)


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='test@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'
