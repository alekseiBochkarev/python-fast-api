from pydantic import BaseModel, HttpUrl
from sqlalchemy import Column, Integer, String, Boolean
from models.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    avatar = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

