from sqlalchemy import Column, ForeignKey, UniqueConstraint
from src.utilities.database import Base

from src.models.bus_book import BusBook
from src.models.veterans import Veteran


class BusBookUser(Base):
    __tablename__ = 'BUS_BOOKS_USERS'
    user_id = Column(ForeignKey(Veteran.id), nullable=False)
    book_id = Column(ForeignKey(BusBook.id), nullable=False)
    __table_args__ = (UniqueConstraint(user_id, book_id))
