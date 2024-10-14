from pydantic import BaseModel
from typing import Optional, List

class Salesman(BaseModel):
    id: int
    first_name: str
    last_name: str
    total_sales: int

    class Config:
        orm_mode = True
        
class SalesmanCreate(BaseModel):
    first_name: str
    last_name: str

class ContactReport(BaseModel):
    id: int
    report_date: str
    report: str
    next_contact: str

    class Config:
        orm_mode = True

class ContactReportCreate(BaseModel):
    report: str
    next_contact: str