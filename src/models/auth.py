from sqlalchemy import Column, String, JSON, Integer
from src.utilities.database import Base


class Auth(Base):
    __tablename__ = "AUTHENTICATION_AUTHORIZATION"
    user_id = Column(Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    password = Column(String, nullable=False)
    roles = Column(JSON, nullable=False)
    username = Column(String, nullable=False, unique=True)
