from sqlalchemy.orm import Session
from database.models import person as models
from database.schemas import person as schemas

def get_person(db: Session, person_id: int):
    return db.query(models.PersonModel).filter(models.PersonModel.id == person_id).first()

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PersonModel).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.PersonModel(first_name=person.first_name, last_name=person.last_name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_contact_number(db: Session, contact_number: schemas.ContactNumberCreate, person_id: int):
    combined_number = f"{(contact_number.code)}-{contact_number.number}"
    db_contact_number = models.ContactNumberModel(number=combined_number, person_id=person_id)
    db.add(db_contact_number)
    db.commit()
    db.refresh(db_contact_number)
    return db_contact_number