from src.models.veterans import Veteran
from src.models.contact_sheet import ContactSheet
from src.models.medical_sheet import MedicalSheet
from sqlalchemy.orm import Session


def get_veteran(db: Session, id: int):
    return db.query(Veteran).get(id)


def create_veteran(db: Session, fname: str, mi: str, lname: str, guardian: int, details: dict, contact: dict, medical: dict):
    veteran = Veteran(
        first_name=fname,
        last_name=lname,
        middle_initial=mi,
        guardian=guardian,
        details=details
    )
    db.add(veteran)
    db.commit()
    db.flush()
    db.refresh(veteran)
    contact_sheet = ContactSheet(
        user=veteran.id,
        primary_phone=contact["p_phone"],
        primary_addr=contact["p_addr"],
        phones=contact["phones"],
        emergency=contact["emergency"],
        email=contact["email"]
    )
    db.add(contact_sheet)
    db.commit()
    db.flush()
    db.refresh(contact_sheet)
    medical_sheet = MedicalSheet(
        user=veteran.id,
        training=medical["training"],
        conditions=medical["conditions"],
        diet=medical["diet"],
        comments=medical["comments"]
    )
    db.add(medical_sheet)
    db.commit()
    db.flush()
    db.refresh(medical_sheet)
    db.refresh(veteran)
    return veteran
