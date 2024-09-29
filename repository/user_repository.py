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
    
    def get_user(self, user_id: int) -> UserBase:
        self.db.query(UserBase).filter(UserBase.user_id == user_id).first()

    def delete_user(self, user: UserBase) -> bool:
        self.db.delete(user)
        self.db.commit()
        return True