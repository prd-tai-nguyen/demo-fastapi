from models.post_model import PostModel
from schemas.post_schema import PostCreate
from repo.base_repo import BaseRepo
import json

class PostRepo(BaseRepo):
    def get_post(self, post_id: int):
        return self.db.query(PostModel).filter(PostModel.id == post_id).first()

    def get_posts(self, limit: int = 10, skip: int = 0 , **kwargs):
        query = self.db.query(PostModel)
       
        # if "email" in kwargs:
        #     query = query.filter(UserModel.email == kwargs['email'])
        # if "name" in kwargs:
        #     query = query.filter(UserModel.name == kwargs['name'])

        return query.offset(skip).limit(limit).all()

    def create_post(self, post_data: PostCreate, user_id: int):
        db_item = PostModel(**post_data.dict(), user_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update_post(self, post_data: PostCreate, post_id: int, user_id: int):
        query = self.db.query(PostModel).filter(PostModel.id == post_id)
        if(post is None):
            return None

        post = query.update(post_data.dict())
        return post
    
    def delete_post(self, post_id: int, user_id: int):
        post = self.db.query(PostModel).filter(PostModel.id == post_id)
        if(query is None):
            return None

        query = self.db.delete(post)
        return query

post_repo = PostRepo()