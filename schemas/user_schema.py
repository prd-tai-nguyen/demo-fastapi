from pydantic import BaseModel
from typing import List
from .post_schema import Post


class UserCreate(BaseModel):
    email: str
    password: str
    name: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    is_active: bool
    posts: List[Post] = []


class User(BaseModel):
    id: int
    email: str
    name: str
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
