from models.user_model import UserModel
from repo.base_repo import BaseRepo
import json

class UserRepo(BaseRepo):
    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_users(self, limit: int = 10, skip: int = 0 , **kwargs):
        query = self.db.query(UserModel)
       
        if "email" in kwargs:
            query = query.filter(UserModel.email == kwargs['email'])
        if "name" in kwargs:
            query = query.filter(UserModel.name == kwargs['name'])

        return query.offset(skip).limit(limit).all()

user_repo = UserRepo()