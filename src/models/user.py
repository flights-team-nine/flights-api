from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from src.models.base import Base


class User(Base):
    __tablename__ = "USERS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    middle_initial = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    guardian = Column(ForeignKey(id), nullable=True)
    details = Column(JSON, nullable=True)
