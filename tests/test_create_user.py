import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza con el nombre de tu aplicación FastAPI

client = TestClient(app)

@pytest.fixture
def create_existing_user():
    # Dado que no estoy registrado
    # Creamos un usuario existente en la base de datos para simular el caso
    user_data = {
        "email": "test@example.com",
        "name": "Existing User",
        "password": "securepassword"
    }
    client.post("/users", json=user_data)
    return user_data

def test_register_with_existing_email(create_existing_user):
    # When me quiero registrar con un email que ya existe previamente
    response = client.post("/users", json={
        "email": create_existing_user["email"],
        "name": "New User",
        "password": "anotherpassword"
    })

    # Then no puedo registrarme en la aplicación
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"