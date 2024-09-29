from repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from tables.user_base import UserBase, UserUpdate

class UserService:

   def __init__(self,
                 db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, user: UserBase):
       
    def get_user(self, user_id: int):
       
    def get_users(self):

    def update_user(self, user: UserUpdate):
       
    def delete_user(self, user: UserBase):