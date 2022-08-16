from models import PostModel, CommentModel
from schemas.post_schema import PostCreate
from repo.base_repo import BaseRepo


class PostRepo(BaseRepo):
    def find_by_id(self, post_id: int, user_id: int):
        return self.db.query(PostModel).filter(PostModel.id == post_id, PostModel.user_id == user_id).first()

    def find(self, limit: int, skip: int, user_id: int = None):
        query = self.db.query(PostModel)
        return query.filter(PostModel.user_id == user_id).offset(skip).limit(limit).all()

    def find_comment(self, user_id: int = None, post_id: int = None):
        query = self.db.query(PostModel)

        return query.filter(PostModel.user_id == user_id, post_id == post_id).first()

    def create(self, data: PostCreate, user_id: int):
        db_item = PostModel(**data.dict(), user_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, data: PostCreate, post_id: int, user_id: int):
        result = self.db.query(PostModel).filter(
            PostModel.id == post_id, PostModel.user_id == user_id).update(data.dict())
        if (result == 0):
            return None

        return result

    def delete(self, post_id: int, user_id: int):
        post = self.db.query(PostModel).filter(
            PostModel.id == post_id, PostModel.user_id == user_id)
        if post is None:
            return None
        
        self.db.query(CommentModel).filter(
            CommentModel.post_id == post_id, CommentModel.user_id == user_id).delete()
        post.delete()

        return True


post_repo = PostRepo()
