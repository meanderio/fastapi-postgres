from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float
)
from database import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Purchases(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    amount = Column(Float)
    purchaser_id = Column(Integer, ForeignKey('users.id'))
