from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from typing import List, Optional

class HouseModel(Base):
    __tablename__ = "house"

    id : Mapped[int] = mapped_column(primary_key=True)
    address : Mapped[str]
    location : Mapped[str]
    price : Mapped[int]
    owner_id : Mapped[int] = mapped_column(ForeignKey("client.id"))
    owner : Mapped["ClientModel"] = relationship("ClientModel", back_populates="houses")

from .client import ClientModel