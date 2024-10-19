import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza con el nombre de tu aplicación FastAPI
from service.exceptions.users_exceptions import *
from database import get_database, Base, engine


@pytest.fixture(scope="module")
def client():
    # Set up the in-memory SQLite database
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)

def create_existing_user(client):
    user_data = {
        "email": "test@example.com",
        "name": "Existing User",
        "password": "securepassword"
    }
    client.post("/users", json=user_data)
    return user_data

def test_register_with_existing_email(client):
    user = create_existing_user(client)
    response = client.post("/users", json={
        "email": user["email"],
        "name": "New User",
        "password": "anotherpassword"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == MESSAGE_USER_ALREADY_REGISTERED

def test_register_without_name(client):
    response = client.post("/users", json={
        "email": "test@example.com",
        "password": "anotherpassword"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == MESSAGE_USER_HAVE_NOT_NAME

def test_register_with_valid_email_and_password(client):
    user_data = {
        "email": "newuser@example.com",
        "name": "New User",
        "password": "securepassword"
    }

    response = client.post("/users", json=user_data)

    assert response.status_code == 201  # User created successfully
    assert response.json()["email"] == user_data["email"]