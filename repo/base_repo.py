from models.user_model import UserModel
from config.db import SessionLocal, engine

UserModel.metadata.create_all(bind=engine)

class BaseRepo:  
    def __init__(self):
        db = SessionLocal()
        try:
            self.db = db
        finally:
            db.close()