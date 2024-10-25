from sqlalchemy.orm import Session
from database.models import houses as models
from database.schemas import houses as schemas

# create
def create_house(db: Session, house: schemas.HouseCreate):
    db_house = models.HouseModel(address=house.address, location=house.location, price=house.price, owner_id=house.owner_id, region=house.region)
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

# read
def get_house(db: Session, house_id: int):
    return db.query(models.HouseModel).filter(models.HouseModel.id == house_id).first()

def get_houses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HouseModel).offset(skip).limit(limit).all()

# update
def update_house_price(db: Session, house_id: int, new_price: int):
    if new_price <= 0:
        return {"message": "Invalid price"}
    house = db.query(models.HouseModel).filter(models.HouseModel.id == house_id)
    if not house.first():
        return {"message": "House not found"}
    house.update({"price": new_price})
    db.commit()
    return {"message": "House updated successfully"}

def update_house_location(db: Session, house_id: int, new_location: str):
    if new_location == "" or new_location.isspace():
        return {"message": "Invalid location"}
    house = db.query(models.HouseModel).filter(models.HouseModel.id == house_id)
    if not house.first():
        return {"message": "House not found"}
    house.update({"location": new_location})
    db.commit()
    return {"message": "House updated successfully"}

def update_house_address(db: Session, house_id: int, new_address: str):
    if new_address == "" or new_address.isspace():
        return {"message": "Invalid address"}
    house = db.query(models.HouseModel).filter(models.HouseModel.id == house_id)
    if not house.first():
        return {"message": "House not found"}
    house.update({"address": new_address})
    db.commit()
    return {"message": "House updated successfully"}

# delete
def delete_house(db: Session, house_id: int):
    house = db.query(models.HouseModel).filter(models.HouseModel.id == house_id)
    if not house.first():
        return {"message": "House not found"}
    house.delete()
    db.commit()
    return {"message": "House deleted successfully"}