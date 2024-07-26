from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'token_type' in token
    assert 'access_token' in token


def test_get_token_com_usuario_desconhecido(client):
    response = client.post(
        '/auth/token',
        data={'username': 'test', 'password': 'test'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_com_senha_invalido(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': 'test'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}
