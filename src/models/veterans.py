from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from src.utilities.database import Base


class Veteran(Base):
    __tablename__ = "VETERANS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    middle_initial = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    guardian = Column(ForeignKey(id), nullable=True)
    details = Column(JSON, nullable=True)
    medical = relationship("MedicalSheet", back_populates="user")
    contact = relationship("ContactSheet", back_populates="user")
