from sqlalchemy import Column, Float, ForeignKey, Integer, String

from db.database import Base


class Purchases(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    amount = Column(Float)
    purchaser_id = Column(Integer, ForeignKey("users.id"))
