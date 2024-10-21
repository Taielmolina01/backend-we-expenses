from repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from models.user import UserModel, UserUpdate, UserResponseModel
from tables.user_base import UserBase
from service.exceptions.users_exceptions import *

def create_user_from_model(user_model: UserModel) -> UserBase:
    return UserBase(
        email=user_model.email,
        name=user_model.name,
        balance=user_model.balance,
        password=user_model.password  # Make sure to hash the password before storing it
    )

class UserService:

    def __init__(self,
                db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self,
                    user: UserModel) -> UserResponseModel:
        registered_user = self.user_repository.get_user(user.email)
        if registered_user:
           raise UserAlreadyRegistered(user.email)
        if not user.name:
           raise UserWithoutName()
        return self.user_repository.create_user(create_user_from_model(user))
       
    def get_user(self, 
                 user_email: str) -> UserResponseModel:
        user = self.user_repository.get_user(user_email)
        if not user:
            raise UserNotRegistered(user_email)
        return user
       
    def get_users(self) -> list[UserResponseModel]:
       return self.user_repository.get_users()

    def update_user(self, 
                    user_email: str, 
                    user_update: UserUpdate) -> UserResponseModel:
        user = self.get_user(user_email)
        if user_update.name:
            user.name = user_update.name
        if user_update.balance:
            user.balance = user_update.balance
        return self.user_repository.update_user(create_user_from_model(user))
        
       
    def delete_user(self, 
                    user: UserBase) -> bool:
       user = self.get_user(user.email)
       return self.user_repository.delete_user(user.email)