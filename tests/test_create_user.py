import pytest
from fastapi.testclient import TestClient
from main import app 
from service.exceptions.users_exceptions import *
from pytest_bdd import scenario, given, when, then
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from models.user import UserModel

@scenario('../features/create_user.feature', 'Registro con un email existente')
def test_register_with_existing_email():
    pass

@scenario('../features/create_user.feature', 'Registro con un email inexistente')
def test_register_with_valid_email_and_password():
    pass

@given("estoy registrado")
def given_user_registered(session):
    pass

@given("no estoy registrado")
def given_user_not_registered():
    # Asumimos que la base de datos está limpia o que no existe el usuario a registrar.
    pass

@when("me quiero registrar con un email que ya existe previamente")
def when_register_with_existing_email(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )
    userService = UserService(session)
    userService.create_user(user_data)
    with pytest.raises(UserAlreadyRegistered):
        userService.create_user(user_data)

@then("no puedo registrarme en la aplicación")
def then_cannot_register(session):
    user = UserService(session).get_user("test@example.com")
    assert user.email == "test@example.com"
    assert user.name == "Existing User"

@when("tengo un email válido e ingreso la contraseña deseada y la confirmo")
def when_register_with_valid_email(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )
    UserService(session).create_user(user_data)

@then("puedo registrar mi usuario y contraseña en la aplicación")
def then_can_register(session):
    user = UserService(session).get_user("test@example.com")
    assert user.email == "test@example.com"
    assert user.name == "Existing User"