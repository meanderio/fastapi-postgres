from typing import Optional, List

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from db.database import Base
from sqlmodel import Field, SQLModel, Relationship


class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    purchases: List["Purchases"] = Relationship(back_populates="purchaser")


# class Users(Base):
#    __tablename__ = "users"
#    id = Column(Integer, primary_key=True, index=True)
#    name = Column(String, index=True)
#    purchases = relationship("Purchases", back_populates="purchaser")
#
#    class Config:
#        from_attributes = True
