from pydantic import BaseModel


class PurchaseBase(BaseModel):
    location: str
    amount: float
    name: str
