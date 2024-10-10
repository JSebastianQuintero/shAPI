from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from typing import List

class PersonModel(Base):
    __tablename__ = "person"

    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    contact_numbers : Mapped[List["ContactNumberModel"]] = relationship("ContactNumberModel", back_populates="person")
    
class ContactNumberModel(Base):
    __tablename__ = "contact_number"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    number : Mapped[str]
    person_id : Mapped[int] = mapped_column(ForeignKey("person.id"))
    person: Mapped["PersonModel"] = relationship("PersonModel", back_populates="contact_numbers")