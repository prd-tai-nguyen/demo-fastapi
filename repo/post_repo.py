from models.post_model import PostModel
from schemas.post_schema import PostCreate
from repo.base_repo import BaseRepo
import json

class PostRepo(BaseRepo):
    def find_by_id(self, post_id: int, user_id: int):
        return self.db.query(PostModel).filter(PostModel.id == post_id, PostModel.user_id == user_id).first()

    def find(self, limit: int = 10, skip: int = 0, user_id: int = None, **kwargs):
        query = self.db.query(PostModel)
       
        # if "email" in kwargs:
        #     query = query.filter(UserModel.email == kwargs['email'])
        # if "name" in kwargs:
        #     query = query.filter(UserModel.name == kwargs['name'])

        return query.filter(PostModel.user_id == user_id).offset(skip).limit(limit).all()

    def create(self, post_data: PostCreate, user_id: int):
        db_item = PostModel(**post_data.dict(), user_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, post_data: PostCreate, post_id: int, user_id: int):
        result = self.db.query(PostModel).filter(PostModel.id == post_id, PostModel.user_id == user_id).update(post_data.dict())
        if(result == 0):
            return None

        return result
    
    def delete(self, post_id: int, user_id: int):
        result = self.db.query(PostModel).filter(PostModel.id == post_id, PostModel.user_id == user_id).delete()
        if(result == 0):
            return None

        return result

post_repo = PostRepo()