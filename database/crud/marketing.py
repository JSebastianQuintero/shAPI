from sqlalchemy.orm import Session
from database.models import marketing as models
from database.schemas import marketing as schemas

from datetime import datetime
# create 
def create_salesman(db: Session, salesman: schemas.SalesmanCreate):
    db_salesman = models.SalesmanModel(first_name=salesman.first_name, last_name=salesman.last_name, total_sales=0)
    db.add(db_salesman)
    db.commit()
    db.refresh(db_salesman)
    return db_salesman

def create_contact_report(db: Session, contact_report: schemas.ContactReportCreate, salesman_id: int):
    db_contact_report = models.ContactReportModel(report_date=datetime.now(), report=contact_report.report, next_contact=contact_report.next_contact, salesman_id=salesman_id)
    db.add(db_contact_report)
    db.commit()
    db.refresh(db_contact_report)
    return db_contact_report

def create_house_post(db: Session, house_post: schemas.HousePostCreate):
    db_house_post = models.HousePostModel(**house_post.model_dump())
    db.add(db_house_post)
    db.commit()
    db.refresh(db_house_post)
    return db_house_post

# read
def get_salesman(db: Session, salesman_id: int):
    salesman = db.query(models.SalesmanModel).filter(models.SalesmanModel.id == salesman_id).first()
    if not salesman:
        return {"message": "Salesman not found"}
    return salesman 

def get_salesmen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SalesmanModel).offset(skip).limit(limit).all()

def get_contact_reports(db: Session, salesman_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.ContactReportModel).filter(models.ContactReportModel.salesman_id == salesman_id).offset(skip).limit(limit).all()

def get_house_posts(db: Session):
    return db.query(models.HousePostModel).all()

# update 
# delete
def delete_salesman(db: Session, salesman_id: int):
    salesman = db.query(models.SalesmanModel).filter(models.SalesmanModel.id == salesman_id)
    if not salesman.first():
        return {"message": "Salesman not found"}
    else:
        name = f"{salesman.first().first_name} {salesman.first().last_name}"
        salesman.delete()
    db.commit()
    return {"message": f"{name} deleted"}

def delete_contact_report(db: Session, contact_report_id: int):
    db.query(models.ContactReportModel).filter(models.ContactReportModel.id == contact_report_id).delete()
    db.commit()
    return {"message": "Contact report deleted"}

def delete_house_post(db: Session, house_post_id: int):
    house_post = db.query(models.HousePostModel).filter(models.HousePostModel.id == house_post_id).delete()
    if not house_post:
        return {"message": "House post not found"}
    db.commit()
    return {"message": "House post deleted"}