from pydantic import BaseModel
from typing import Optional, List

class HouseBase(BaseModel):
    price: int
    owner_id: int  
    location: Optional[str] = None
    address: Optional[str] = None

class HouseCreate(HouseBase):
    pass

class House(HouseBase):
    id: int
        
    class Config:
        orm_mode = True