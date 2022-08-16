from models import UserModel, PostModel, CommentModel
from config.db import SessionLocal, engine

UserModel.metadata.create_all(bind=engine)
PostModel.metadata.create_all(bind=engine)
CommentModel.metadata.create_all(bind=engine)

class BaseRepo:  
    def __init__(self):
        db = SessionLocal()
        try:
            self.db = db
        finally:
            db.close()