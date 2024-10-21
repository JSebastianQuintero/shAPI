from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.crud import client as crud
from database.schemas import client as schemas
from database.models import client as model
from database.database import SessionLocal, engine, get_db

model.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.get("/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

@router.get("/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.post("/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@router.post("/{client_id}/contact_number", response_model=schemas.ContactNumber)
def create_contact_number(client_id: int, contact_number: schemas.ContactNumberCreate, db: Session = Depends(get_db)):
    return crud.create_contact_number(db=db, contact_number=contact_number, client_id=client_id)

@router.delete("/{client_id}", response_model=dict)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    resp = crud.delete_client(db=db, client_id=client_id)
    if resp is "Client not found":
        raise HTTPException(status_code=404, detail="Client not found")
    return resp

@router.delete("/contact_number/{contact_number_id}", response_model=dict)
def delete_contact_number(contact_number_id: int, db: Session = Depends(get_db)):
    resp = crud.delete_contact_number(db=db, contact_number_id=contact_number_id)
    if resp is "Contact number not found":
        raise HTTPException(status_code=404, detail="Contact number not found")
    return resp