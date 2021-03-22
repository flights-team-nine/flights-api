from sqlalchemy import Column, ForeignKey, UniqueConstraint
from src.models.base import Base

from src.models.bus_book import BusBook
from src.models.user import User


class BusBookUser(Base):
    __tablename__ = 'BUS_BOOKS_USERS'
    user_id = Column(ForeignKey(User.id), nullable=False)
    book_id = Column(ForeignKey(BusBook.id), nullable=False)
    __table_args__ = (UniqueConstraint(user_id, book_id))
