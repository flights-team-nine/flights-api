from sqlalchemy import Column, Integer, String, ForeignKey
from src.utilities.database import Base

from src.models.bus_book import BusBook


class Team(Base):
    __tablename__ = 'TEAMS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    bus_book = Column(ForeignKey(BusBook.id), nullable=False)
