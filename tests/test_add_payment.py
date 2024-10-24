from pytest_bdd import scenario, given, when, then
import pytest
from fastapi.testclient import TestClient
from main import app
from service.user_service import UserService
from service.group_service import GroupService
from service.payment_service import PaymentService
from service.users_by_groups_service import UserByGroupService
from models.user import UserModel
from util_functions import *
from service.debt_service import DebtService
from models.payment import Category

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
    UserService(session).create_user(create_user_model())

@given("soy parte de un evento/grupo en el que soy el único participante")
def single_participant_event(session):
  user = UserModel(email="single_user@example.com", name="Single User", balance=0, password="password")
  user_service = UserService(session)
  user_base = user_service.create_user(user)
  group_base = GroupService(session).create_group(create_group_model())
  UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base, group_base))

@given("soy parte de un evento/grupo en el que hay más de un participante")
def multiple_participants_event(session):
  # Create an event/group with multiple users
  user_service = UserService(session)
  user_base_one = user_service.create_user(create_user_model())
  user_base_two = user_service.create_user(create_user_model_2())
  group_base = GroupService(session).create_group(create_group_model())
  UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_one, group_base))
  UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_two, group_base))

@when("agrego mis gastos")
def add_expense_not_part_of_event():
  pass

@when("agrego mis gastos siendo el único integrante")
def add_expense_single_participant(session):
  user_base = UserService(session).get_user("single_user@example.com")
  group_base = GroupService(session).get_group(1)
  PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.ENTERTAINMENT), {user_base.email: 1})

@when("agrego que realicé un gasto de X")
def add_expense_multiple_participants(session):
  user_base_one = UserService(session).get_user("test@example.com")
  user_base_two = UserService(session).get_user("test2@example.com")
  group_base = GroupService(session).get_group(1)
  PaymentService(session).create_payment(create_payment_model(user_base_one, group_base, Category.EDUCATION), {user_base_one.email: 0.5, user_base_two.email: 0.5})

@then("no agrego mis gastos")
def cannot_add_expense():
  # Verify that the expense was not added
  pass

@then("mi saldo actual sigue siendo el previo")
def balance_remains_same(session):
  user_base = UserService(session).get_user("single_user@example.com")
  user = UserService(session).get_user(user_base.email)
  assert user.balance == 0
  assert user.email == "single_user@example.com"
  assert user.name == "Single User"

@then("el gasto del grupo aumenta en X")
def group_expense_increases(session):
  user_base_one = UserService(session).get_user("test@example.com")
  user_base_two = UserService(session).get_user("test2@example.com")
  group_base = GroupService(session).get_group(1)
  debt_by_creditor = DebtService(session).get_debts_by_creditor(user_base_one.email)[0]
  debt_by_debtor = DebtService(session).get_debts_by_debtor(user_base_two.email)[0]
  assert debt_by_creditor.group_id == debt_by_debtor.group_id == group_base.group_id
  assert debt_by_creditor.creditor_email == debt_by_debtor.creditor_email
  assert debt_by_creditor.debtor_email == debt_by_debtor.debtor_email
  assert debt_by_creditor.debt_id == debt_by_debtor.debt_id
  assert debt_by_creditor.payment_id == debt_by_debtor.payment_id 
  assert debt_by_creditor.percentage == debt_by_debtor.percentage
  assert user_base_one.balance == - 0.5 * 200
  assert user_base_two.balance == debt_by_debtor.percentage * 200
