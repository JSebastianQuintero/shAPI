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

class HousePostBase(BaseModel):
    name : str
    starting_price : int
    bedrooms : int
    bathrooms : int
    covered_area : int
    semicovered_area : int
    living_room : bool
    kitchen : bool
    dining_room : bool
    garage : bool
    pergola : bool
    gallery : bool
    img_path: str
class HousePost(HousePostBase):
    id: int
    class Config:
        orm_mode = True

class HousePostCreate(HousePostBase):
    pass
class ContactBase(BaseModel):
    name: str
    email: str
    message: Optional[str] = None

class Contact(ContactBase):
    id: int
    phone: str
    class Config:
        orm_mode = True
        
class ContactCreate(ContactBase):
    code: int
    number: int