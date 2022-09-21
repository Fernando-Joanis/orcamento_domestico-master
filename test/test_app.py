
def test_app_is_created(app):
    assert app.name == 'api'


def test_config_is_loaded(config):
    assert config['DEBUG'] is False


def test_request_returns_200(client):
    assert client.get('/api/despesas').status_code == 200


def test_request_post_returns_200(client):
    data = {
        'valor': 2000,
        'descricao': 'Água',
        'data_compra': '2022-09-05',
        'tipo_pagamento_id': 1,
        'categoria_id': 1
              }
    assert client.post('/api/despesas', data=data).status_code == 200
