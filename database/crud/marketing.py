from sqlalchemy.orm import Session
from database.models import marketing as models
from database.schemas import marketing as schemas

def get_salesman(db: Session, salesman_id: int):
    return db.query(models.SalesmanModel).filter(models.SalesmanModel.id == salesman_id).first()

def get_salesmen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SalesmanModel).offset(skip).limit(limit).all()

def create_salesman(db: Session, salesman: schemas.SalesmanCreate):
    db_salesman = models.SalesmanModel(first_name=salesman.first_name, last_name=salesman.last_name, total_sales=0)
    db.add(db_salesman)
    db.commit()
    db.refresh(db_salesman)
    return db_salesman

# def create_contact_report(db: Session, contact_report: schemas.ContactReportModelCreate, salesman_id: int):
#     db_contact_report = models.ContactReportModel(report_date=contact_report.report_date, report=contact_report.report, next_contact=contact_report.next_contact, salesman_id=salesman_id)
#     db.add(db_contact_report)
#     db.commit()
#     db.refresh(db_contact_report)
#     return db_contact_report