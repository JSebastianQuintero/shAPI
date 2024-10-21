from sqlalchemy.orm import Session
from database.models import client as models
from database.schemas import client as schemas
# create 
def create_client(db: Session, client: schemas.ClientCreate):
    db_person = models.ClientModel(first_name=client.first_name, last_name=client.last_name , location=client.location)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_contact_number(db: Session, contact_number: schemas.ContactNumberCreate, client_id: int):
    new_number = f"{contact_number.code}-{contact_number.number}"
    db_contact_number = models.ContactNumberModel(number=new_number, client_id=client_id)
    db.add(db_contact_number)
    db.commit()
    db.refresh(db_contact_number)
    return db_contact_number

# read
def get_client(db: Session, client_id: int):
    return db.query(models.ClientModel).filter(models.ClientModel.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClientModel).offset(skip).limit(limit).all()

def get_contact_numbers(db: Session, client_id: int):
    db_client = db.query(models.ClientModel).filter(models.ClientModel.id == client_id).first()
    if not db_client:
        return {"message": "Client not found"}
    return db.query(models.ContactNumberModel).filter(models.ContactNumberModel.client_id == client_id).all()

# update 
def update_client_first_name(db: Session, client_id: int, new_name: str):
    if new_name == "" or new_name.isspace():
        return {"message": "Invalid name"}
    client = db.query(models.ClientModel).filter(models.ClientModel.id == client_id)
    if not client.first():
        return {"message": "Client not found"}
    client.update({"first_name": new_name})
    db.commit()
    return {"message": "Client updated successfully"}

def update_client_last_name(db: Session, client_id: int, new_name: str):
    if new_name == "" or new_name.isspace():
        return {"message": "Invalid name"}
    client = db.query(models.ClientModel).filter(models.ClientModel.id == client_id)
    if not client.first():
        return {"message": "Client not found"}
    client.update({"last_name": new_name})
    db.commit()
    return {"message": "Client updated successfully"}

def update_client_location(db: Session, client_id: int, new_location: str):
    if new_location == "" or new_location.isspace():
        return {"message": "Invalid location"}
    client = db.query(models.ClientModel).filter(models.ClientModel.id == client_id)
    if not client.first():
        return {"message": "Client not found"}
    client.update({"location": new_location})
    db.commit()
    return {"message": "Client updated successfully"}

# delete
def delete_client(db: Session, client_id: int):
    client = db.query(models.ClientModel).filter(models.ClientModel.id == client_id)
    if not client.first():
        return {"message": "Client not found"}
    client.delete()
    db.commit()
    return {"message": "Client deleted successfully"}

def delete_contact_number(db: Session, contact_number_id: int):
    contact_number = db.query(models.ContactNumberModel).filter(models.ContactNumberModel.id == contact_number_id)
    if not contact_number.first():
        return {"message": "Contact number not found"}
    contact_number.delete()
    db.commit()
    return {"message": "Contact number deleted successfully"}