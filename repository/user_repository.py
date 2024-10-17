from sqlalchemy.orm import Session
from tables.user_base import UserBase
from models.user import UserModel, UserUpdate

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, 
                    user: UserModel):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_users(self) -> list[UserBase]:
        return self.db.query(UserBase).all()

    def get_user(self, 
                 email: str) -> UserBase:
        return self.db.query(UserBase).filter(UserBase.email == email).first()
    
    def update_user(self, 
                    user: UserUpdate) -> UserBase:
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, 
                    user: UserModel) -> bool:
        self.db.delete(user)
        self.db.commit()
        return True