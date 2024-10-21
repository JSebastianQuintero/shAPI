from pydantic import BaseModel
from typing import Optional, List

class ContactNumberCreate(BaseModel):
    code: int
    number: int

class ContactNumber(BaseModel):
    id: int
    client_id: int
    number: str  

    class Config:
        orm_mode = True
        
class ClientBase(BaseModel):
    first_name: str
    last_name: str
    location: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True