from pydantic import BaseModel
from typing import Optional, List

class ContactNumberBase(BaseModel):
    code: str
    number: str

class ContactNumberCreate(ContactNumberBase):
    pass

class ContactNumber(BaseModel):
    id: int
    person_id: int
    number: str  

    class Config:
        orm_mode = True
        
class PersonBase(BaseModel):
    first_name: str
    last_name: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    contact_numbers: List[ContactNumber] = []

    class Config:
        orm_mode = True