from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.base import Base

from src.models.mission import Mission


class BusBook(Base):
    __tablename__ = 'BUS_BOOKS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    mission = Column(ForeignKey(Mission.id), nullable=False)
