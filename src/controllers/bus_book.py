from datetime import datetime
from src.models.bus_book import BusBook
from sqlalchemy.orm import Session


def get_bus_books(db: Session, mission_id: int):
    return db.query(BusBook).filter(BusBook.mission == mission_id).all()


def create_bus_book(db: Session, name: str, mission: int, driver: int, destination: str, arrival: datetime, departure: datetime):
    book = BusBook(
        mission=mission,
        name=name,
        driver=driver,
        destination=destination,
        arrival=arrival,
        departure=departure
    )
    db.add(book)
    db.commit()
    db.flush()
    db.refresh(book)
    return book


def update_bus_book(db: Session, id: int, name=None, mission=None, driver=None, destination=None, arrival=None, departure=None):
    book = db.query(BusBook).get(id)
    if name != None or mission != None:
        if name != None and book.name != name:
            book.name = name
        if mission != None and book.mission != mission:
            book.mission = mission
        if driver != None and book.driver != driver:
            book.driver = driver
        if destination != None and book.destination != destination:
            book.destination = destination
        if arrival != None and book.arrival != arrival:
            book.arrival = arrival
        if departure != None and book.departure != departure:
            book.departure = departure
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
