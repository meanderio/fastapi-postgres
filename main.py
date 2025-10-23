from fastapi import (
    FastAPI,
    HTTPException,
    Depends
)
from pydantic import BaseModel
from typing import (
    List,
    Annotated
)
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    name: str

class PurchaseBase(BaseModel):
    location: str
    amount: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/")
async def create_user(user: UserBase, db:db_dependency):
    db_user = models.Users(
            name=user.name
    )
    db.add(db_user)
    db.commit()

@app.post("/purchases/")
async def create_purchase(purchase: PurchaseBase, db: db_dependency):
    db_purchase = models.Purchases(
        location=purchase.location,
        amount=purchase.amount
    )
    db.add(db_purchase)
    db.commit()
