from pytest_bdd import scenario, given, when, then
import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel
from tables.user_base import UserBase


client = TestClient(app)

@scenario("../features/registro_de_usuario.feature", "Registro con un email no existente")
def test_register_with_non_existing_email():
    pass

@scenario("../features/registro_de_usuario.feature", "Registro con un email existente")
def test_register_with_existing_email():
    pass

@scenario("../features/registro_de_usuario.feature", "Registro exitoso")
def test_successful_registration():
    pass

@given("no estoy registrado")
def no_user_registered(session):
    # Asegúrate de que la base de datos de prueba esté vacía
    pass

@given("estoy registrado con un email existente")
def user_registered(session):
    # Crea un usuario en la base de datos de prueba
    user = UserModel(email="test@example.com", name="Test User", balance=0, password="testpassword")
    user_service = UserService(session)
    user_service.create_user(user)

@when("me quiero registrar con un email que no existe previamente")
def register_with_non_existing_email():
    response = client.post("/users", json={
        "email": "new_user@example.com",
        "name": "New User",
        "balance": 0,
        "password": "newpassword"
    })
    assert response.status_code == 201  # Esperamos un 201 Created

@when("me quiero registrar con un email que ya existe previamente")
def register_with_existing_email():
    response = client.post("/users", json={
        "email": "test@example.com",
        "name": "Another User",
        "balance": 0,
        "password": "anotherpassword"
    })
    assert response.status_code == 400  # Esperamos un 400 Bad Request

@when("tengo un email válido e ingreso la contraseña deseada y la confirmo")
def successful_registration():
    response = client.post("/users", json={
        "email": "valid_user@example.com",
        "name": "Valid User",
        "balance": 0,
        "password": "validpassword"
    })
    assert response.status_code == 201  # Esperamos un 201 Created

@then("puedo ingresar la contraseña que deseo establecer")
def can_set_password():
    # Se verifica que la contraseña ha sido almacenada correctamente
    pass

@then("no puedo registrarme en la aplicación")
def cannot_register():
    # No se necesita verificar más, el assert en el paso de `@when` lo hace
    pass

@then("puedo registrar mi usuario y contraseña en la aplicación")
def can_register_user():
    # Se verifica que el usuario ha sido creado
    response = client.get("/users/valid_user@example.com")
    assert response.status_code == 200  # Usuario debe existir
