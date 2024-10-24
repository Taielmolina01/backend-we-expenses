import pytest
from fastapi.testclient import TestClient
from main import app 
from service.exceptions.users_exceptions import *
from pytest_bdd import scenario, given, when, then
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from service.exceptions.groups_exceptions import *
from models.user import UserModel
from models.group import GroupModel
from service.group_service import GroupService

@scenario('../features/update_grupo.feature', 'Actualizar siendo un usuario no registrado')
def test_update_group_with_unregistered_user():
    pass

@scenario('../features/update_grupo.feature', 'Actualizar siendo un usuario registrado un grupo inexistente')
def test_update_unregistered_group_with_registered_user():
    pass

@scenario('../features/update_grupo.feature', 'Actualizo siendo un usuario registrado con datos inválidos un grupo existente')
def test_update_with_invalid_fields_registered_group_with_registered_user():
    pass

@scenario('../features/update_grupo.feature', 'Actualizo siendo un usuario registrado con datos válidos un grupo existente')
def test_update_with_valid_fields_registered_group_with_registered_user():
    pass

@given("no estoy registrado")
def given_user_not_registered():
    pass

@given("estoy registrado y no existe mi grupo")
def given_user_registered(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )
    userService = UserService(session)
    userService.create_user(user_data)

@given("estoy registrado y existe mi grupo")
def given_user_registered_and_group(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )
    userService = UserService(session)
    userService.create_user(user_data)  
    group_data = GroupModel(
        name="MyGroup"
    )
    GroupService(session).create_group(group_data)

@when("actualizo mi grupo")
def update_group(session):
    update_group_data = GroupModel(
        name="NewName"
    )
    GroupService(session).update_group(1, update_group_data)

@when("actualizo mi grupo inexistente")
def update_unregistered_group(session):
    update_group_data = GroupModel(
        name="NewName"
    )
    with pytest.raises(GroupNotRegistered):
        GroupService(session).update_group(1, update_group_data)

@when("actualizo mi grupo con datos inválidos")
def update_registered_group_with_invalid_fields(session):
    update_group_data = GroupModel(
        name=""
    )
    with pytest.raises(GroupWithoutName):
        GroupService(session).update_group(1, update_group_data)

@when("actualizo mi grupo con datos válidos")
def update_registered_group_with_valid_fields(session):
    update_group_data = GroupModel(
        name="NewName"
    )
    GroupService(session).update_group(1, update_group_data)

@then("se me indica que no estoy registrado")
def not_registered_user(session):
    pass

@then("se me indica que no existe el grupo")
def not_registered_group(session):
    pass

@then("no se actualiza")
def dont_update(session):
    pass

@then("se actualiza")
def dont_update(session):
    pass

