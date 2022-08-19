from models import CommentModel, PostModel
from schemas.comment_schema import CommentCreate, CommentUpdate
from repo.base_repo import BaseRepo


class CommentRepo(BaseRepo):
    def find_by_id(self, comment_id: int):
        return self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()

    def create(self, data: CommentCreate, user_id: int):
        post = self.db.query(PostModel).filter(
            PostModel.id == data.post_id, PostModel.user_id == user_id).first()
        if post is None:
            return None

        db_item = CommentModel(**data.dict(), user_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, data: CommentUpdate, user_id: int, comment_id: int):
        result = self.db.query(CommentModel).filter(
            CommentModel.id == comment_id, PostModel.user_id == user_id).update(data.dict())
        if (result == 0):
            return None

        return result

    def delete(self, comment_id: int, user_id: int):
        result = self.db.query(CommentModel).filter(
            CommentModel.id == comment_id, CommentModel.user_id == user_id).delete()

        if (result == 0):
            return None

        return result


comment_repo = CommentRepo()
