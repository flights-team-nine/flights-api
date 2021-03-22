from sqlalchemy import Column, ForeignKey, String, JSON
from src.models.base import Base

from src.models.user import User


class MedicalSheet(Base):
    __tablename__ = "MEDICAL_SHEETS"
    user_id = Column(ForeignKey(User.id), nullable=False, unique=True)
    training = Column(JSON, nullable=True)
    conditions = Column(JSON, nullable=True)
    diet = Column(JSON, nullable=True)
    comments = Column(String, nullable=True)
