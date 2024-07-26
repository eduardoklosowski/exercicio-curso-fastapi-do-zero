from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html_deve_retornar_ok_e_pagina_html(client):
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<title>Nosso olá mundo!</title>' in response.text
    assert '<h1>Olá Mundo!</h1>' in response.text
