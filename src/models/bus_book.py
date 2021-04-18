from sqlalchemy.sql.sqltypes import DateTime
from src.models.veterans import Veteran
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.utilities.database import Base


class BusBook(Base):
    __tablename__ = 'BUS_BOOKS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    mission = relationship("Mission", back_populates="bus_books")
    driver = Column(ForeignKey(Veteran.id), nullable=False)
    destination = Column(String(255), nullable=False)
    arrival = Column(DateTime(timezone=True), nullable=False)
    departure = Column(DateTime(timezone=True), nullable=False)
    teams = relationship("Team", back_populates="bus_books")
