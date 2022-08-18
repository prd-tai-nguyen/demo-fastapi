from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="posts")
    comments = relationship("CommentModel", back_populates="post")