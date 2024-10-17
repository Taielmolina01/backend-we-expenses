from repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from models.user import UserModel, UserUpdate
from tables.user_base import UserBase
from service.exceptions.users_exceptions import *

class UserService:

    def __init__(self,
                db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self,
                    user: UserModel) -> UserBase:
        registered_user = self.get_user(user.email)
        if registered_user:
           raise UserAlreadyRegistered(user.email)
        if not user.name:
           raise UserWithoutName()
        # balance puede crearse con algo distinto a 0?
        return self.user_repository.create_user(user)
       
    def get_user(self, 
                 user_email: str) -> UserBase:
        user = self.user_repository.get_user(user_email)
        if user is None:
            raise UserNotRegistered(user_email)
        return user
       
    def get_users(self) -> list[UserBase]:
       return self.user_repository.get_users()

    def update_user(self, 
                    user_email: str, 
                    user_update: UserUpdate) -> UserBase:
        user = self.get_user(user_email)
        if user_update.name is not None:
            user.name = user_update.name
        if user_update.balance is not None:
            user.balance = user_update.balance
        return self.user_repository.update_user(user)
        
       
    def delete_user(self, 
                    user: UserBase) -> bool:
       user = self.get_user(user.email)
       return self.user_repository.delete_user(user.email)