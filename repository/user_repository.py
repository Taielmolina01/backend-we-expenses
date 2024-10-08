from sqlalchemy.orm import Session
from tables.user_base import UserBase

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserBase):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_users(self) -> list[UserBase]:
        return self.db.query(UserBase).all()

    def get_user(self, mail: str) -> UserBase:
        return self.db.query(UserBase).filter(UserBase.mail == mail).first()
    
    def update_user(self, user: UserBase) -> UserBase:
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user: UserBase) -> bool:
        self.db.delete(user)
        self.db.commit()
        return True