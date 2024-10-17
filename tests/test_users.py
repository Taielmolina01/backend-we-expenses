import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import get_database

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users",
        json={
            "email": "test@example.com",
            "name": "Test User",
            "balance": 100,
            "password": "password123"
        }
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_user():
    response = client.get("/users/test@example.com")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_user_not_found():
    response = client.get("/users/nonexistent@example.com")
    assert response.status_code == 404

def test_login():
    response = client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    assert response.json() is True

def test_login_invalid_user():
    response = client.post(
        "/login",
        json={
            "email": "nonexistent@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 404

def test_update_user():
    response = client.put(
        "/users/test@example.com",
        json={
            "name": "Updated Test User",
            "balance": 150
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Test User"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200

def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404