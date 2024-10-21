from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.crud import houses as crud
from database.schemas import houses as schemas
from database.models import houses as model
from database.database import SessionLocal, engine, get_db

model.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/houses", tags=["Houses"])

# read
@router.get("/", response_model=list[schemas.House])
def read_houses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    houses = crud.get_houses(db, skip=skip, limit=limit)
    return houses

@router.get("/{house_id}", response_model=schemas.House)
def read_house(house_id: int, db: Session = Depends(get_db)):
    db_house = crud.get_house(db, house_id=house_id)
    if db_house is None:
        raise HTTPException(status_code=404, detail="House not found")
    return db_house

# create
@router.post("/", response_model=schemas.House)
def create_house(house: schemas.HouseCreate, db: Session = Depends(get_db)):
    return crud.create_house(db=db, house=house)

# update
@router.put("/{house_id}/price", response_model=dict)
def update_house(house_id: int, new_price: int, db: Session = Depends(get_db)):
    return crud.update_house_price(db=db, house_id=house_id, new_price=new_price)

@router.put("/{house_id}/location", response_model=dict)
def update_house_location(house_id: int, new_location: str, db: Session = Depends(get_db)):
    return crud.update_house_location(db=db, house_id=house_id, new_location=new_location)

@router.put("/{house_id}/address", response_model=dict)
def update_house_address(house_id: int, new_address: str, db: Session = Depends(get_db)):
    return crud.update_house_address(db=db, house_id=house_id, new_address=new_address)

# delete
@router.delete("/{house_id}", response_model=dict)
def delete_house(house_id: int, db: Session = Depends(get_db)):
    return crud.delete_house(db=db, house_id=house_id)