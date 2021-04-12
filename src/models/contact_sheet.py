from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
from src.utilities.database import Base

from src.models.veterans import Veteran


class ContactSheet(Base):
    __tablename__ = "CONTACT_SHEETS"
    user = relationship("Veteran", back_populates="contact")
    primary_phone = Column(String, nullable=False, unique=True)
    primary_addr = Column(String, nullable=False)
    phones = Column(JSON, nullable=True)
    emergency = Column(ForeignKey(Veteran.id), nullable=False)
    email = Column(String, nullable=False)
