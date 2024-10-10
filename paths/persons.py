from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.crud import person as crud
from database.schemas import person as schemas
from database.models import person as model
from database.database import SessionLocal, engine, get_db

model.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.get("/", response_model=list[schemas.Person])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    persons = crud.get_persons(db, skip=skip, limit=limit)
    return persons

@router.get("/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@router.post("/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db=db, person=person)

@router.post("/{person_id}/contact_number", response_model=schemas.ContactNumber)
def create_contact_number(person_id: int, contact_number: schemas.ContactNumberCreate, db: Session = Depends(get_db)):
    return crud.create_contact_number(db=db, contact_number=contact_number, person_id=person_id)