from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class Purchases(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    location: str = Field(index=True)
    amount: float
    purchaser_id: Optional[int] = Field(default=None, foreign_key="users.id")
    purchaser: Optional["Users"] = Relationship(back_populates="purchases")


# class Purchases(Base):
#    __tablename__ = "purchases"
#    id = Column(Integer, primary_key=True, index=True)
#    location = Column(String, index=True)
#    amount = Column(Float)
#    purchaser_id = Column(Integer, ForeignKey("users.id"))
#    purchaser = relationship("Users", back_populates="purchases")
#
#    class Config:
#        from_attributes = True
