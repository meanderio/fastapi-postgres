from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.purchase import Purchase


class UserBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    purchases: list["Purchase"] = Relationship(back_populates="purchaser")


class UserPublic(UserBase):
    id: int


class UserPublicWithPurchases(UserPublic):
    purchases: list["Purchase"] = []


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: str | None = None
