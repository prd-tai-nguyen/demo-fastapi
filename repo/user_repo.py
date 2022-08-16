from models import UserModel
from repo.base_repo import BaseRepo

class UserRepo(BaseRepo):
    def find_by_id(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def find(self, limit: int, skip: int , **kwargs):
        query = self.db.query(UserModel)
       
        if "email" in kwargs:
            query = query.filter(UserModel.email == kwargs['email'])
        if "name" in kwargs:
            query = query.filter(UserModel.name == kwargs['name'])

        return query.offset(skip).limit(limit).all()

    def find_post(self, limit: int = 10, skip: int = 0 , user_id: int= None, **kwargs):
        user = self.db.query(UserModel).filter(UserModel.id == user_id).offset(skip).limit(limit).first()
        return user

user_repo = UserRepo()