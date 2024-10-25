from pydantic import BaseModel
from typing import Optional, List
from ..models.houses import regionOptions, lineOptions
class HouseBase(BaseModel):
    price: int
    owner_id: int  
    location: Optional[str] = None
    address: Optional[str] = None
    region: regionOptions
    line: lineOptions 
class HouseCreate(HouseBase):
    pass

class House(HouseBase):
    id: int
        
    class Config:
        orm_mode = True