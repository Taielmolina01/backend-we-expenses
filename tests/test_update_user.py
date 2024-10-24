import pytest
from fastapi.testclient import TestClient
from main import app 
from service.exceptions.users_exceptions import *
from pytest_bdd import scenario, given, when, then
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from models.user import UserModel

@scenario('../features/update_user.feature', 'Actualizar un usuario inexistente')
def test_update_unregistered_user():
    pass

@scenario('../features/update_user.feature', 'Actualizar un usuario existente con datos inválidos')
def test_update_registered_user_with_invalid_fields():
    pass

@scenario('../features/update_user.feature', 'Actualizar un usuario existente con datos válidos')
def test_update_registered_user_with_valid_feilds():
    pass

@given("no estoy registrado")
def given_user_not_registered():
    pass

@given("estoy registrado")
def given_user_registered(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )
    userService = UserService(session)
    userService.create_user(user_data)

@when("actualizo mi perfil")
def when_register_with_existing_email(session):
    pass # no se bien como hacerlo aca

@then("se me indica que no existe el usuario")
def then_cannot_register(session):
    user_data = UserModel(
    name="Existing User",
    balance=100
    )
    with pytest.raises(UserNotRegistered):
        UserService(session).update_user("test@example.com", user_data)

@when("actualizo mi perfil con datos inválidos")
def when_register_with_valid_email(session):
    user_data = UserModel(
        name=""
    )
    UserService(session).update_user("test@example.com", user_data)

@when("actualizo mi perfil con datos inválidos")
def when_register_with_valid_email(session):
    user_data = UserModel(
        name="MyNewName"
    )
    UserService(session).update_user("test@example.com", user_data)

@then("no se actualiza")
def then_can_register(session):
    user = UserService(session).get_user("test@example.com")
    assert user.email == "test@example.com"
    assert user.name == "Existing User"
    assert user.balance == 0

@then("se actualiza")
def then_can_register(session):
    user = UserService(session).get_user("test@example.com")
    assert user.email == "test@example.com"
    assert user.name == "MyNewName"
    assert user.balance == 0