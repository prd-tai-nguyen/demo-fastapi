from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    test2 = Column(String(255))

    posts = relationship("PostModel", back_populates="user")