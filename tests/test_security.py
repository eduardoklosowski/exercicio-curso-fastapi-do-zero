from datetime import UTC, datetime

import jwt
from fast_zero.security import SECRET_KEY, create_access_token, get_password_hash, verify_password


def test_jwt():
    data = {'test': 'test'}

    token = create_access_token(data)

    decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert datetime.fromtimestamp(decoded['exp'], UTC) > datetime.now(UTC)


def test_senha():
    pwd = 'test'

    hash_ = get_password_hash(pwd)

    assert verify_password(pwd, hash_)


def test_senha_invalida():
    hash_ = get_password_hash('test1')

    assert not verify_password('test2', hash_)
