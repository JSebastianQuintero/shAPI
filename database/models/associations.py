from sqlalchemy import Table, Column, Integer, ForeignKey
from ..database import Base

client_house_association = Table(
    'client_house_association',
    Base.metadata,
    Column('client_id', Integer, ForeignKey('client.id')),
    Column('house_id', Integer, ForeignKey('house.id'))
)