from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import Annotated

from database.crud import marketing as crud
from database.schemas import marketing as schemas
from database.models import marketing as model
from database.database import SessionLocal, engine, get_db

model.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/marketing", tags=["Marketing"])

# files

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "file_location": file_location}

# routes

@router.get("/salesmans/", response_model=list[schemas.Salesman])
def read_salesmen(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    salesmen = crud.get_salesmen(db, skip=skip, limit=limit)
    return salesmen

@router.get("/salesmans/{salesman_id}", response_model=schemas.Salesman)
def read_salesman(salesman_id: int, db: Session = Depends(get_db)):
    db_salesman = crud.get_salesman(db, salesman_id=salesman_id)
    if db_salesman is None:
        raise HTTPException(status_code=404, detail="Salesman not found")
    return db_salesman

@router.get("/salesmans/{salesman_id}/contact-reports", response_model=list[schemas.ContactReport])
def read_contact_reports(salesman_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contact_reports(db, salesman_id=salesman_id, skip=skip, limit=limit)

@router.get("/house-posts", response_model=list[schemas.HousePost])
def read_house_posts(db: Session = Depends(get_db)):
    return crud.get_house_posts(db)

@router.post("/salesmans/", response_model=schemas.Salesman)
def create_salesman(salesman: schemas.SalesmanCreate, db: Session = Depends(get_db)):
    return crud.create_salesman(db=db, salesman=salesman)

@router.post("/salesmans/{salesman_id}/contact-report", response_model=schemas.ContactReport)
def create_contact_report(salesman_id: int, contact_report: schemas.ContactReportCreate, db: Session = Depends(get_db)):
    return crud.create_contact_report(db=db, contact_report=contact_report, salesman_id=salesman_id)

@router.post("/house-posts", response_model=schemas.HousePost)
def create_house_post(house_post: schemas.HousePostCreate, db: Session = Depends(get_db)):
    return crud.create_house_post(db=db, house_post=house_post)

@router.delete("/salesmans/{salesman_id}", response_model=dict)
def delete_salesman(salesman_id: int, db: Session = Depends(get_db)):
    return crud.delete_salesman(db=db, salesman_id=salesman_id)

@router.delete("/contact-report/{contact_report_id}", response_model=dict)
def delete_contact_report(contact_report_id: int, db: Session = Depends(get_db)):
    return crud.delete_contact_report(db=db, contact_report_id=contact_report_id)

@router.delete("/house-post/{house_post_id}", response_model=dict)
def delete_house_post(house_post_id: int, db: Session = Depends(get_db)):
    return crud.delete_house_post(db=db, house_post_id=house_post_id)