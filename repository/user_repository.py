from sqlalchemy.orm import Session
from tables.user_base import UserBase
from models.user import UserModel, UserUpdate, UserResponseModel

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_response_model(self, user: UserBase) -> UserResponseModel:
        return UserResponseModel(email=user.email,
                                name=user.name,
                                balance=user.balance,
        )

    def create_user(self, 
                    user: UserBase) -> UserResponseModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_users(self) -> list[UserResponseModel]:
        return self.db.query(UserBase).all()

    def get_user(self, 
                 email: str) -> UserResponseModel:
        return self.db.query(UserBase).filter(UserBase.email == email).first()
    
    def update_user(self, 
                    user: UserBase) -> UserResponseModel:
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, 
                    user: UserBase) -> bool:
        self.db.delete(user)
        self.db.commit()
        return True