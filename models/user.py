from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(index=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: str | None = None


# class Users(SQLModel, table=True):
#    id: Optional[int] = Field(primary_key=True, index=True)
#    name: str
#    age: Optional[int]
#    # purchases: List["Purchases"] = Relationship(back_populates="purchaser")
