from sqlalchemy import Column, String, JSON, ForeignKey
from src.models.base import Base

from src.models.user import User


class User(Base):
    __tablename__ = "USERS"
    user_id = Column(ForeignKey(User.id), nullable=False, unique=True)
    password = Column(String, nullable=False)
    roles = Column(JSON, nullable=False)
