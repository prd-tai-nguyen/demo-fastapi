from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255), unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="posts")