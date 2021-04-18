from src.models.veterans import Veteran
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.utilities.database import Base

from src.models.bus_book import BusBook


class Team(Base):
    __tablename__ = 'TEAMS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    color = Column(String(32), nullable=False)
    bus_books = relationship("BusBook", back_populates="teams")
    members = relationship("Veteran", back_populates="team")
    leader = Column(ForeignKey(Veteran.id), nullable=False)
