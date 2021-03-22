from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from src.models.base import Base

from src.models.user import User


class ContactSheet(Base):
    __tablename__ = "CONTACT_SHEETS"
    user_id = Column(ForeignKey(User.id), nullable=False, unique=True)
    primary_phone = Column(String, nullable=False, unique=True)
    primary_addr = Column(String, nullable=False)
    phones = Column(JSON, nullable=True)
    emergency = Column(ForeignKey(User.id), nullable=False)
    email = Column(String, nullable=False)
