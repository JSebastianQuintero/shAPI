from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from .client import ClientModel

class SalesmanModel(Base):
    __tablename__ = "salesman"

    id : Mapped[int] = mapped_column( primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    contact_reports : Mapped[List["ContactReportModel"]] = relationship("ContactReportModel", back_populates="salesman")
    total_sales : Mapped[int]

class ContactReportModel(Base):
    __tablename__ = "contact_report"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    report_date : Mapped[str]
    report : Mapped[str]
    next_contact : Mapped[str]
    salesman_id : Mapped["SalesmanModel"] = mapped_column(ForeignKey("salesman.id"))
    salesman: Mapped["SalesmanModel"] = relationship("SalesmanModel", back_populates="contact_reports")
    