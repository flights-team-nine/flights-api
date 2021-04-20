from src.models.teams import Team
from sqlalchemy.orm import Session


def get_teams(db: Session, book_id: int):
    return db.query(Team).filter(Team.bus_book == book_id).all()


def create_team(db: Session, name: str, color: str, bus_book: int):
    team = Team(
        name=name,
        color=color,
        bus_book=bus_book
    )
    db.add(team)
    db.commit()
    db.flush()
    db.refresh(team)
    return team


def update_team(db: Session, id: int, name=None, color=None, bus_book=None, leader=None):
    team = db.query(Team).get(id)
    if name != None or color != None or bus_book != None:
        if name != None and team.name != name:
            team.name = name
        if color != None and team.color != color:
            team.color = color
        if bus_book != None and team.bus_books != bus_book:
            team.bus_book = bus_book
        if leader != None and team.leader != leader:
            team.leader = leader
        db.commit()
        db.flush()
        db.refresh(team)
    return team


def delete_team(db: Session, id: int):
    team = db.query(Team).get(id)
    db.delete(team)
    db.commit()
    db.flush()
    return team.id
