from typing import Optional

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    age: Optional[int]
    # purchases: List["Purchases"] = Relationship(back_populates="purchaser")
