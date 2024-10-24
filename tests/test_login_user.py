import pytest
from fastapi.testclient import TestClient
from main import app 
from service.exceptions.users_exceptions import *
from pytest_bdd import scenario, given, when, then
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from models.user import UserModel

# aca deberia usar algo distinto a como vengo testeando porque no se pueden solo probar los servicios como tal,
# maybe el login deberia tener un servicio y ahi lo arreglo y listo

@scenario('../features/login_user.feature', 'No estoy registrado')
def test_not_registered():
    pass

@scenario('../features/login_user.feature', 'Estoy registrado e ingreso mal la contraseña')
def test_registered_and_wrong_password():
    pass

@scenario('../features/login_user.feature', 'Estoy registrado e ingreso bien la contraseña')
def test_registered_and_correct_password():
    pass

@given("estoy registrado")
def given_user_registered(session):
    pass

@given("no estoy registrado")
def given_user_not_registered():
    # Asumimos que la base de datos está limpia o que no existe el usuario a registrar.
    pass

@when("inicio sesión")
def when_register_with_existing_email(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )

@when("inicio sesión")
def when_register_with_existing_email(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )

@when("inicio sesión")
def when_register_with_existing_email(session):
    user_data = UserModel(
        email="test@example.com",
        name="Existing User",
        password="securepassword"
    )

@when("quiero iniciar sesión e ingreso mal mi contraseña")
def when_login_with_wrong_password(session):
    pass

@when("quiero iniciar sesión e ingreso bien mi contraseña")
def when_login_with_correct_password(session):
    pass

@then("no puedo iniciar sesión")
def then_can_not_login(session):
    pass

@then("puedo iniciar sesión")
def then_can_login(session):
    pass