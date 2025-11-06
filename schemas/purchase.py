from pydantic import BaseModel

from schemas.user import UserPublic


class PurchaseBase(BaseModel):
    location: str
    amount: float
    name: str


class PurchasePublic(PurchaseBase):
    id: int


class PurchaseWithUser(PurchasePublic):
    purchaser: UserPublic | None = None
