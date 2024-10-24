from pytest_bdd import scenario, given, when, then
import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.group_service import GroupService
from models.group import GroupModel
from models.user import UserModel
from tables.group_base import GroupBase
from tables.user_base import UserBase

client = TestClient(app)

@scenario("../features/update_group.feature", "Cambiar nombre siendo administrador")
def test_change_name_as_admin():
    pass

@scenario("../features/update_group.feature", "Cambiar nombre sin ser administrador")
def test_change_name_not_as_admin():
    pass

@scenario("../features/update_group.feature", "Cambiar foto siendo administrador")
def test_change_name_as_admin():
    pass

@scenario("../features/update_group.feature", "Cambiar foto sin ser administrador")
def test_change_name_not_as_admin():
    pass


@given("soy administrador del grupo")
def admin_of_group(session):
    # Crear un usuario administrador y un grupo en la base de datos de prueba
    admin_user = UserModel(email="admin@example.com", name="Admin User", balance=0, password="adminpassword")
    group = GroupModel(name="Old Group Name", admin_id=admin_user.id)
    session.add(admin_user)
    session.add(group)
    session.commit()

@given("no soy administrador del grupo")
def not_admin_of_group(session):
    # Crear un usuario no administrador y un grupo en la base de datos de prueba
    non_admin_user = UserModel(email="user@example.com", name="Regular User", balance=0, password="userpassword")
    admin_user = UserModel(email="admin@example.com", name="Admin User", balance=0, password="adminpassword")
    group = GroupModel(name="Old Group Name", admin_id=admin_user.id)
    session.add(non_admin_user)
    session.add(admin_user)
    session.add(group)
    session.commit()

@when("cambio el nombre del grupo y lo confirmo")
def change_group_name_as_admin():
    response = client.put("/groups/1", json={
      "name": "New Group Name",
      "admin_id": 1  # ID del administrador
    })
    assert response.status_code == 200  # Esperamos un 200 OK

@when("intento cambiar el nombre del grupo")
def try_change_group_name_not_as_admin():
    response = client.put("/groups/1", json={
      "name": "New Group Name",
      "admin_id": 2  # ID del usuario no administrador
    })
    assert response.status_code == 403  # Esperamos un 403 Forbidden

@then("el nombre del grupo se actualiza correctamente")
def group_name_updated_correctly():
    response = client.get("/groups/1")
    assert response.status_code == 200
    assert response.json()["name"] == "New Group Name"

@then("no puedo cambiarlo y me avisa que no tengo permisos")
def cannot_change_group_name():
    response = client.get("/groups/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Old Group Name"