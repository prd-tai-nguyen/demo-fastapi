from pydantic import BaseModel
from typing import List
from .comment_schema import Comment


class PostCreate(BaseModel):
    content: str


class PostResponse(BaseModel):
    id: int
    content: str
    user_id: int


class Post(BaseModel):
    id: int
    content: str
    user_id: int
    comments: List[Comment]

    class Config:
        orm_mode = True
