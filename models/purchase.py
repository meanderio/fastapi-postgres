from sqlmodel import Field, Relationship, SQLModel

from models.user import User


class PurchaseBase(SQLModel):
    location: str = Field(index=True)
    amount: float
    user_id: int | None = Field(default=None, foreign_key="user.id")


class Purchase(PurchaseBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    purchaser: User | None = Relationship(back_populates="purchases")


class PurchasePublic(PurchaseBase):
    id: int


class PurchasePublicWithUser(PurchasePublic):
    purchaser: User | None = None


class PurchaseCreate(PurchaseBase):
    pass


class PurchaseUpdate(PurchaseBase):
    location: str | None = None
    amount: str | None = None
    user_id: int | None = None


# class Purchases(SQLModel, table=True):
#    id: Optional[int] = Field(primary_key=True, index=True)
#    location: str = Field(index=True)
#    amount: float
#    purchaser_id: Optional[int] = Field(default=None, foreign_key="users.id")
#    # purchaser: Optional["Users"] = Relationship(back_populates="purchases")
