from datetime import UTC, datetime
from http import HTTPStatus

import jwt
from fast_zero.security import SECRET_KEY, create_access_token, get_password_hash, verify_password


def test_jwt():
    data = {'test': 'test'}

    token = create_access_token(data)

    decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert datetime.fromtimestamp(decoded['exp'], UTC) > datetime.now(UTC)


def test_jwt_invalid_token(client):
    response = client.delete('/users/1', headers={'Authorization': 'Bearer token-invalido'})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_sem_usuario(client):
    token = create_access_token({})

    response = client.delete('/users/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_com_usuario_desconhecido(client):
    token = create_access_token({'sub': 'test'})

    response = client.delete('/users/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_senha():
    pwd = 'test'

    hash_ = get_password_hash(pwd)

    assert verify_password(pwd, hash_)


def test_senha_invalida():
    hash_ = get_password_hash('test1')

    assert not verify_password('test2', hash_)
