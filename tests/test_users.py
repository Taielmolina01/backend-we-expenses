import pytest
from fastapi.testclient import TestClient
from main import app  # Replace with your app's entry point
from models.user import UserModel, UserUpdate  # Replace with your models
from service.user_service import UserService  # Replace with your service
from service.exceptions.users_exceptions import UserAlreadyRegistered, UserWithoutName, UserNotRegistered
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from controller.user_controller import hash_password

DATABASE_URL = "sqlite:///:memory:"

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Create a new SQLite database in memory for testing
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Initialize the database, create tables, etc. here

    yield  # This allows the tests to run

    # Cleanup (if necessary) after tests complete

def test_create_user(setup_database):
    response = client.post("/users", 
                           json={
                            "email": "test@example.com",
                            "name": "Test User",
                            "balance": 100,
                            "password": "password123"
                            })
    assert response.status_code == 200
    assert response.json() == {
                            "email": "test@example.com",
                            "name": "Test User",
                            "balance": 100,
                            "password": hash_password("password123") 
    }