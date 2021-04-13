from sqlalchemy import Column, ForeignKey, String, JSON
from sqlalchemy.orm import relationship
from src.utilities.database import Base

from src.models.veterans import Veteran


class MedicalSheet(Base):
    __tablename__ = "MEDICAL_SHEETS"
    user = relationship("Veteran", back_populates="medical")
    training = Column(JSON, nullable=True)
    conditions = Column(JSON, nullable=True)
    diet = Column(JSON, nullable=True)
    comments = Column(String, nullable=True)
