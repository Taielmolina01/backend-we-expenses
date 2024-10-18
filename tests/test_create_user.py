from pytest_bdd import scenario, given, when, then
import pytest
from models.user import UserModel
from service.user_service import *
from  pydantic_core import ValidationError
from datetime import datetime

@pytest.fixture
def new_user():
    return UserModel(
        email="nuevousuario@example.com",
        name="Nuevo Usuario",
        balance=0.0,
        password="contraseña123"
    )

@pytest.fixture
def existing_user(db):
    user = UserModel(
        email="usuarioexistente@example.com",
        name="Usuario Existente",
        balance=0.0,
        password="contraseña123"
    )
    return UserService(db).create_user(user)

@scenario("../features/create_user.feature", "Registro con un email existente")
def create_user_registered():
    pass

@scenario("../features/create_user.feature", "Registro con un email inexistente")
def create_user_not_registered():
    pass

@given("no estoy registrado")
def no_registered_user(db, new_user):
    # Asegurémonos de que el usuario no exista en la base de datos
    UserService(db).delete_user(new_user.email)

@when("me quiero registrar con un email que ya existe previamente")
def register_with_existing_email(client, existing_user):
    response = client.post("/users", json=existing_user.dict())
    global response_existing_user
    response_existing_user = response

@then("no puedo registrarme en la aplicación")
def cannot_register_with_existing_email():
    assert response_existing_user.status_code == 400  # Ajusta el código de estado según tu implementación

@when("tengo un email válido e ingreso la contraseña deseada y la confirmo")
def register_with_valid_data(client, new_user):
    response = client.post("/users", json=new_user.dict())
    global response_new_user
    response_new_user = response

@then("puedo registrar mi usuario y contraseña en la aplicación")
def can_register_new_user():
    assert response_new_user.status_code == 200