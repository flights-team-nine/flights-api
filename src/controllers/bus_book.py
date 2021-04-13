from src.models.bus_book import BusBook
from sqlalchemy.orm import Session


def get_bus_books(db: Session, mission_id: int):
    return db.query(BusBook).filter(BusBook.mission == mission_id).all()


def create_bus_book(db: Session, name: str, mission: int):
    book = BusBook(
        mission=mission,
        name=name
    )
    db.add(book)
    db.commit()
    db.flush()
    db.refresh(book)
    return book


def update_bus_book(db: Session, id: int, name=None, mission=None):
    book = db.query(BusBook).get(id)
    if name != None or mission != None:
        if name != None and book.name != name:
            book.name = name
        if mission != None and book.mission != mission:
            book.mission = mission
        db.commit()
        db.flush()
        db.refresh(book)
    return book


def delete_bus_book(db: Session, id: int):
    book = db.query(BusBook).get(id)
    db.delete(book)
    db.commit()
    db.flush()
    return book.id
