from sqlalchemy.orm import Session
from repository.payment_repository import PaymentRepository
from models.payment import PaymentModel, PaymentUpdate
from tables.payment_base import PaymentBase
from service.exceptions.payments_exceptions import *
from service.users_by_groups_service import UserByGroupService
from service.debt_service import DebtService
from service.user_service import UserService
from models.debt import DebtModel, DebtUpdate
from models.user import UserUpdate
from tables.user_base import UserBase

def create_payment_from_model(payment_model: PaymentModel) -> PaymentBase:
    return PaymentBase(
        group_id = payment_model.group_id,
        payer_email = payment_model.payer_email,
        date = payment_model.date,
        category = payment_model.category,
        amount = payment_model.amount
    )

class PaymentService:

    def __init__(self,
                 db: Session):
        self.payment_repository = PaymentRepository(db)
        self.user_by_group = UserByGroupService(db)
        self.debt_service = DebtService(db)
        self.user_service = UserService(db)

    def create_payment(self,
                       payment: PaymentModel,
                       percentages: dict[str, float]) -> PaymentBase:
        users = self.user_by_group.get_users_by_group(payment.group_id)
        if len(percentages) > len(users):
            raise PaymentWithMoreDistributionsThanGroupUsers()
        if len(users) > len(percentages):
            raise PaymentWithLessDistributionsThanGroupUsers()
        for u in users:
            if u.user_email == payment.payer_email:
                self.user_service.update_user(user.user_email, UserUpdate(
                name=user.name,
                balance=user.balance - payment.amount + percentages[user.user_email]
                ))
            else:
                user = self.user_service.get_user(u.user_email)
                self.debt_service.create_debt(DebtModel(payment_id=payment.payment_id, 
                                                        group_id=payment.group_id, 
                                                        debtor_email=user.user_email, 
                                                        creditor_email=payment.payer_email, 
                                                        percentage=percentages[user.user_email]))
                self.__update_user_balance(user, payment, percentages)
        
        return self.payment_repository.create_payment(create_payment_from_model(payment))

        
    def get_payment(self,
                    payment_id: int) -> PaymentBase:
        return self.payment_repository.get_payment(payment_id)
    
    def get_payments_by_group(self,
                              group_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_group(group_id)

    def get_payments_by_user(self,
                              user_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_user(user_id)
    
    def get_payments_by_user_and_group(self,
                              user_id: int,
                              group_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_user_and_group(user_id, group_id)
    
    def __get_original_percentages(self, payment: PaymentBase) -> dict[str, float]:
        debts = self.debt_service.get_debts_by_payment_id(payment.payment_id)
        answer = {}
        for d in debts:
            answer[d.debtor_email] = d.percentage
        return answer

    def update_payment(self,
                    payment_id: int,
                    payment_update: PaymentUpdate,
                    new_percentages: dict[str, float]) -> PaymentBase:
        # Obtener el pago registrado y los usuarios del grupo
        registered_payment = self.get_payment(payment_id)
        if not registered_payment:
            raise PaymentNotRegistered()
        
        # Recuperar los porcentajes originales del pago registrado
        original_percentages = self.__get_original_percentages(registered_payment)
        new_payment = create_payment_from_model(payment_update)
        users = self.user_by_group.get_users_by_group(new_payment.group_id)
        
        # Validar que los porcentajes coincidan con los usuarios
        if len(new_percentages) > len(users):
            raise PaymentWithMoreDistributionsThanGroupUsers()
        if len(users) > len(new_percentages):
            raise PaymentWithLessDistributionsThanGroupUsers()
        
        for u in users:
            user = self.user_service.get_user(u.user_email)
            
            if user.email == new_payment.payer_email:
                # Actualizar el balance del pagador
                # Sumar el pago original para revertir el efecto con el porcentaje original y restar el nuevo pago
                original_share = original_percentages.get(user.email, 0) * registered_payment.amount
                new_share = new_percentages.get(user.email, 0) * new_payment.amount
                updated_balance = user.balance + registered_payment.amount - original_share
                updated_balance -= new_payment.amount - new_share
                self.user_service.update_user(user.user_email, UserUpdate(
                    name=user.name,
                    balance=updated_balance
                ))
            else:
                # Revertir el impacto de la deuda original con el porcentaje original y aplicar la nueva
                original_debt = original_percentages.get(user.email, 0) * registered_payment.amount
                new_debt = new_percentages.get(user.email, 0) * new_payment.amount
                updated_balance = user.balance + original_debt - new_debt

                # Actualizar la deuda en la base de datos
                self.debt_service.update_debt(DebtUpdate(
                    payment_id=new_payment.payment_id,
                    group_id=new_payment.group_id,
                    debtor_email=user.user_email,
                    creditor_email=new_payment.payer_email,
                    percentage=new_percentages[user.email]
                ))
                # Actualizar el balance del usuario
                self.user_service.update_user(user.user_email, UserUpdate(
                    name=user.name,
                    balance=updated_balance
                ))
    
        # Actualizar el pago en la base de datos
        return self.payment_repository.update_payment(new_payment)


    def __update_user_balance(self, user: UserBase, payment: PaymentModel, percentages: list[int]):
        self.user_service.update_user(user.user_email, UserUpdate(
                name=user.name,
                balance=user.balance + percentages[user.email] * payment.amount
        ))

    def delete_payment(self,
                       payment: PaymentModel) -> bool:
        registered_payment = self.get_payment(payment.payment_id)
        if not registered_payment:
            raise PaymentNotRegistered()
        debts = self.debt_service.get_debts_by_payment_id(payment.payment_id)
        for d in debts:
            user = self.user_service.get_user(d.debtor_email)
            self.debt_service.delete_debt(d)
            self.user_service.update_user(user.email, UserUpdate(
                        name=user.name,
                        balance=user.balance - d.percentage * registered_payment.amount
                ))
        payer = self.user_service.get_user(registered_payment.payer_email)
        self.user_service.update_user(payer.payer_email, UserUpdate(
                        name=payer.name,
                        balance=user.balance + registered_payment.amount
                ))
        return self.payment_repository.delete_payment(payment)