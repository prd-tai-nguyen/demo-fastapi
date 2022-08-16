from pydantic import BaseModel


class CommentCreate(BaseModel):
    content: str
    post_id: int

class CommentUpdate(BaseModel):
    content: str

class Comment(BaseModel):
    id: int
    content: str
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
