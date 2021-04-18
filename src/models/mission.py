from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from src.utilities.database import Base


class Mission(Base):
    __tablename__ = 'MISSIONS'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(64), nullable=False, unique=True)
    flight = Column(String(128), nullable=True)
    spotlight = Column(Boolean, nullable=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    bus_books = relationship("BusBook", back_populates="mission")
