from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from typing import List, Optional
from enum import Enum
from .associations import client_house_association

class regionOptions(Enum):
    BUENOSAIRES = "Buenos Aires"
    CORDOBA = "Cordoba"
    
class lineOptions(Enum):
    ECONOMIC = "Economic"
    MEDIUM = "Medium"
    LUXURY = "Luxury"
class HouseModel(Base):
    __tablename__ = "house"

    id : Mapped[int] = mapped_column(primary_key=True)
    address : Mapped[str]
    location : Mapped[str]
    region : Mapped[regionOptions]
    price : Mapped[int]
    owner_id : Mapped[int] = mapped_column(ForeignKey("client.id"))
    owner : Mapped["ClientModel"] = relationship("ClientModel", back_populates="houses")
    visitors: Mapped[List["ClientModel"]] = relationship("ClientModel", secondary=client_house_association, back_populates="visited_houses") 


from .client import ClientModel