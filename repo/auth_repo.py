import hashlib
import jwt
import datetime

from models.user_model import UserModel
from schemas.user_schema import UserCreate
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from repo.base_repo import BaseRepo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthRepo(BaseRepo):
    SECURITY_ALGORITHM = 'HS256'
    SECRET_KEY = '123456'

    def generate_token(self, user_id: str) -> str:
        expire = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=60 * 60 * 24 * 3  # Expired after 3 days
        )

        encoded_jwt = jwt.encode({"exp": expire, "user_id": user_id},
                                 self.SECRET_KEY, algorithm=self.SECURITY_ALGORITHM)
        return encoded_jwt

    def validate_token(self, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[
                                 self.SECURITY_ALGORITHM])
            user = self.db.query(UserModel).filter(
                UserModel.id == payload.get('user_id')).first()

            return user
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=403,
                detail=f"Could not validate credentials",
            )

    def get_user_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def login(self, email: str, password: str):
        user = self.db.query(UserModel).filter(UserModel.email == email, UserModel.hashed_password == hashlib.sha256(
            password.encode('utf-8')).hexdigest()).first()

        if (user == None):
            return None

        return self.generate_token(user.id)

    def register(self, user: UserCreate):
        if (self.get_user_by_email(user.email) is not None):
            return None

        db_user = UserModel(email=user.email, name=user.name, hashed_password=hashlib.sha256(
            user.password.encode('utf-8')).hexdigest())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return self.generate_token(db_user.id)


auth_repo = AuthRepo()
