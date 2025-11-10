from sqlmodel import Field, Relationship, SQLModel

# from models.purchase import Purchase


class UserBase(SQLModel):
    name: str = Field(index=True)


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


# class Users(SQLModel, table=True):
#    id: Optional[int] = Field(primary_key=True, index=True)
#    name: str
#    age: Optional[int]
#    # purchases: List["Purchases"] = Relationship(back_populates="purchaser")
