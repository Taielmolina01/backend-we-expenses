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

@scenario("../features/delete_group.feature", "Borrar grupo siendo administrador")
def test_delete_group_as_admin():
  pass

@scenario("../features/delete_group.feature", "Borrar grupo sin ser administrador")
def test_delete_group_not_as_admin():
  pass

@given("soy administrador del grupo")
def admin_of_group(session):
  # Crear un usuario administrador y un grupo en la base de datos de prueba
  admin_user = UserModel(email="admin@example.com", name="Admin User", balance=0, password="adminpassword")
  group = GroupModel(name="Test Group", admin_id=admin_user.id)
  session.add(admin_user)
  session.add(group)
  session.commit()

@given("no soy administrador del grupo")
def not_admin_of_group(session):
  # Crear un usuario no administrador y un grupo en la base de datos de prueba
  non_admin_user = UserModel(email="user@example.com", name="Regular User", balance=0, password="userpassword")
  admin_user = UserModel(email="admin@example.com", name="Admin User", balance=0, password="adminpassword")
  group = GroupModel(name="Test Group", admin_id=admin_user.id)
  session.add(non_admin_user)
  session.add(admin_user)
  session.add(group)
  session.commit()

@when("selecciono la opción de borrar el grupo")
def delete_group_as_admin():
  response = client.delete("/groups/1", headers={"Authorization": "Bearer admin_token"})
  assert response.status_code == 200  # Esperamos un 200 OK

@when("intento borrar el grupo")
def delete_group_not_as_admin():
  response = client.delete("/groups/1", headers={"Authorization": "Bearer user_token"})
  assert response.status_code == 403  # Esperamos un 403 Forbidden

@then("el grupo se elimina permanentemente y no está disponible en la lista de grupos.")
def group_deleted():
  response = client.get("/groups/1")
  assert response.status_code == 404  # El grupo no debe existir

@then("no puedo borrarlo y me avisa que no tengo permisos.")
def cannot_delete_group():
  # No se necesita verificar más, el assert en el paso de `@when` lo hace
  pass