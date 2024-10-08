from repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from tables.user_base import UserBase, UserUpdate
from exceptions.users_exceptions import * 


class UserService:

    def __init__(self,
                db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self,
                    user: UserBase) -> UserBase:
        registered_user = self.get_user(user.user_id)
        if registered_user is not None:
           raise UserAlreadyRegistered(user.user_id)
        if not user.name:
           raise UserWithoutName()
        # balance puede crearse con algo distinto a 0?
        return self.user_repository.create_user(user)
       
    def get_user(self, 
                 mail_user: str) -> UserBase:
        user = self.user_repository.get_user(mail_user)
        if user is None:
            raise UserNotRegistered(mail_user)
        return user
       
    def get_users(self) -> list[UserBase]:
       return self.user_repository.get_users()

    def update_user(self, 
                    user_id: int, 
                    user_update: UserUpdate) -> UserBase:
        user = self.get_user(user_id)
        if user_update.name is not None:
            user.name = user_update.name
        if user_update.balance is not None:
            user.balance = user_update.balance
        return self.user_repository.update_user(user)
        
       
    def delete_user(self, 
                    user: UserBase) -> bool:
       user = self.get_user(user.user_id)
       return self.user_repository.delete_user(user)