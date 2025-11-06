from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Purchases(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    amount = Column(Float)
    purchaser_id = Column(Integer, ForeignKey("users.id"))
    purchaser = relationship("Users", back_populates="purchases")

    class Config:
        from_attributes = True
