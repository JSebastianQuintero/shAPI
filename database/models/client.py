from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from typing import List, Optional
from .associations import client_house_association
class ClientModel(Base):
    __tablename__ = "client"

    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    location : Mapped[Optional[str]]
    contact_numbers : Mapped[List["ContactNumberModel"]] = relationship("ContactNumberModel", back_populates="client")
    houses : Mapped[List["HouseModel"]] = relationship("HouseModel", back_populates="owner")
    visited_houses: Mapped[List["HouseModel"]] = relationship("HouseModel", secondary=client_house_association, back_populates="visitors")

class ContactNumberModel(Base):
    __tablename__ = "contact_number"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    number : Mapped[str]
    client_id : Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped["ClientModel"] = relationship("ClientModel", back_populates="contact_numbers")

from .houses import HouseModel