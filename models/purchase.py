from typing import Optional

from sqlmodel import Field, SQLModel


class Purchases(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    location: str = Field(index=True)
    amount: float
    purchaser_id: Optional[int] = Field(default=None, foreign_key="users.id")
    # purchaser: Optional["Users"] = Relationship(back_populates="purchases")
