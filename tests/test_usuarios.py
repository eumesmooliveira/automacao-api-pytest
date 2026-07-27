import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_deve_listar_usuarios_com_sucesso():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, list)
    assert len(dados) > 0
    primeiro_usuario = dados[0]
    assert "id" in primeiro_usuario
    assert "name" in primeiro_usuario
    assert "email" in primeiro_usuario

def test_deve_cadastrar_novo_usuario_com_sucesso():
    payload = {
        "name": "Felipe de Oliveira",
        "username": "felipe.qa",
        "email": "felipe@qa.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    resposta_json = response.json()
    assert resposta_json["name"] == payload["name"]
    assert resposta_json["email"] == payload["email"]
    assert "id" in resposta_json

def test_deve_retornar_404_para_usuario_inexistente():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404