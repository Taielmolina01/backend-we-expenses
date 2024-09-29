from sqlalchemy.orm import Session
from tables.user_base import UserBase
from tables.group_base import GroupBase
from tables.users_by_group_base import UserInGroupBase

class UsersByGroupRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_users_by_group(self, group_id: int) -> list[UserBase]:
        return self.db.query(GroupBase).filter(GroupBase.group_id == group_id).all()
    
    def create_user_in_group(self, user_in_group: UserInGroupBase) -> UserInGroupBase:
        self.db.add(user_in_group)
        self.db.commit()
        self.db.refresh(user_in_group)
        return user_in_group
    
    def delete_user_in_group(self, user_in_group: UserInGroupBase) -> bool:
        self.db.delete(user_in_group)
        self.db.commit()
        return True