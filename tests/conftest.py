from urllib.parse import urlparse

import factory
import psycopg
import pytest
from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import Base, User
from fast_zero.security import get_password_hash
from fast_zero.settings import Settings
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from tests.utils import randstr


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}+senha')


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(scope='session')
def engine():
    database_url = urlparse(Settings().DATABASE_URL)
    main_url = database_url._replace(scheme='postgresql').geturl()
    test_database = f'{database_url.path.removeprefix('/')}_test_{randstr(16).lower()}'
    test_url = database_url._replace(path=test_database).geturl()

    main_conn = psycopg.connect(main_url, autocommit=True)
    main_conn.execute(f'CREATE DATABASE {test_database}')

    yield create_engine(test_url)

    main_conn.execute(f'DROP DATABASE {test_database} WITH (FORCE)')
    main_conn.close()


@pytest.fixture()
def session(engine):
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture()
def user(session):
    password = 'testtest'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture()
def other_user(session):
    password = 'testtest2'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture()
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
