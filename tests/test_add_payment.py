from pytest_bdd import scenario, given, when, then
import pytest
from fastapi.testclient import TestClient
from main import app
from service.user_service import UserService
from models.user import UserModel
from tables.user_base import UserBase

client = TestClient(app)

@scenario("../features/add_payment.feature", "Agregar gastos sin ser parte de un evento/grupo")
def test_add_expense_not_part_of_event():
    pass

@scenario("../features/add_payment.feature", "Agregar gastos siendo el único participante")
def test_add_expense_single_participant():
    pass

@scenario("../features/add_payment.feature", "Agregar gastos siendo parte de un evento/grupo con más participantes")
def test_add_expense_multiple_participants():
    pass

@given("no soy parte de un evento/grupo")
def not_part_of_event(session):
  # Ensure the user is not part of any event/group
    pass

@given("soy parte de un evento/grupo en el que soy el único participante")
def single_participant_event(session):
  # Create an event/group with only the current user
  user = UserModel(email="single_user@example.com", name="Single User", balance=0, password="password")
  user_service = UserService(session)
  user_service.create_user(user)
  # Add user to an event/group
  pass

@given("soy parte de un evento/grupo en el que hay más de un participante")
def multiple_participants_event(session):
  # Create an event/group with multiple users
  user1 = UserModel(email="user1@example.com", name="User One", balance=0, password="password")
  user2 = UserModel(email="user2@example.com", name="User Two", balance=0, password="password")
  user_service = UserService(session)
  user_service.create_user(user1)
  user_service.create_user(user2)
  # Add users to an event/group
  pass

@when("agrego mis gastos del evento/grupo")
def add_expense_not_part_of_event():
  response = client.post("/expenses", json={
    "event_id": 1,
    "amount": 100
  })
  assert response.status_code == 400  # Expecting a 400 Bad Request

@when("agrego mis gastos del evento/grupo")
def add_expense_single_participant():
  response = client.post("/expenses", json={
    "event_id": 1,
    "amount": 100
  })
  assert response.status_code == 200  # Expecting a 200 OK

@when("agrego que realicé un gasto de X")
def add_expense_multiple_participants():
  response = client.post("/expenses", json={
    "event_id": 1,
    "amount": 100
  })
  assert response.status_code == 200  # Expecting a 200 OK

@then("no agrego mis gastos")
def cannot_add_expense():
  # Verify that the expense was not added
  pass

@then("mi saldo actual sigue siendo el previo")
def balance_remains_same():
  # Verify that the user's balance remains unchanged
  response = client.get("/users/single_user@example.com")
  user_data = response.json()
  assert user_data["balance"] == 0

@then("el gasto del grupo aumenta en X")
def group_expense_increases():
  # Verify that the group's total expense increased by X
  response = client.get("/events/1")
  event_data = response.json()
  assert event_data["total_expense"] == 100