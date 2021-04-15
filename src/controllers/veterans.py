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


def update_veteran(db: Session, id: int, fname=None, mi=None, lname=None, guardian=None, details=None, contact=None, medical=None):
    veteran = db.query(Veteran).get(id)
    contact_sheet = db.query(ContactSheet).filter(
        ContactSheet.user == veteran.id).first()
    medical_sheet = db.query(MedicalSheet).filter(
        MedicalSheet.user == veteran.id).first()
    if fname != None or mi != None or lname != None or guardian != None or details != None or medical != None or contact != None:
        if fname != None:
            veteran.first_name = fname
        if lname != None:
            veteran.last_name = lname
        if mi != None:
            veteran.middle_initial = mi
        if guardian != None:
            veteran.guardian = guardian
        if details != None:
            veteran.details = details
        if medical != None:
            medical_sheet.training = medical["training"]
            medical_sheet.conditions = medical["conditions"]
            medical_sheet.diet = medical["diet"]
            medical_sheet.comments = medical["comments"]
        if contact != None:
            contact_sheet.primary_phone = contact["p_phone"]
            contact_sheet.primary_addr = contact["p_addr"]
            contact_sheet.phones = contact["phones"]
            contact_sheet.emergency = contact["emergency"]
            contact_sheet.email = contact["email"]
        db.commit()
        db.flush()
        db.refresh(veteran)
        db.refresh(contact_sheet)
        db.refresh(medical_sheet)
    return veteran


def delete_veteran(db: Session, id: int):
    veteran = db.query(Veteran).get(id)
    medical = db.query(MedicalSheet).filter(MedicalSheet.user == id).first()
    contact = db.query(ContactSheet).filter(ContactSheet.user == id).first()
    db.delete(medical)
    db.delete(contact)
    db.delete(veteran)
    db.commit()
    db.flush()
    return veteran.id
