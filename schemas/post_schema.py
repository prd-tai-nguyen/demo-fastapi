from pydantic import BaseModel
from typing import List

class PostCreate(BaseModel):
    content: str

class Post(BaseModel):
    id: int
    content: str
    user_id: int
   
    class Config:
        orm_mode = True