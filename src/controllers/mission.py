from datetime import datetime
from sqlalchemy.orm.session import Session
from src.models.mission import Mission


def get_active_mission(db: Session):
    mission = db.query(Mission).filter(Mission.spotlight).first()
    return mission


def create_mission(db: Session, title: str, flight: str, start: datetime, end: datetime):
    mission = Mission(
        title=title,
        flight=flight,
        start=start,
        spotlight=False,
        end=end
    )
    db.user(mission)
    db.commit()
    db.flush()
    db.refresh(mission)
    return mission


def spotlight_mission(db: Session, id: int, spotlight: bool):
    mission = db.query(Mission).get(id)
    mission.spotlight = spotlight
    db.commit()
    db.flush()
    db.refresh(mission)
    return mission
