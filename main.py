from fastapi import (
    FastAPI,
    HTTPException,
    Depends
)
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import (
    List,
    Annotated
)
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(
    version   = "0.1.0",
    docs_url  = "/docs",
    redoc_url = "/redoc",
)

app.add_middleware(
    CORSMiddleware
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    name: str

class PurchaseBase(BaseModel):
    location: str
    amount: float
    name: str

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
    user = db.query(models.Users).filter(models.Users.name == purchase.name).first()
    db_purchase = models.Purchases(
        location=purchase.location,
        amount=purchase.amount,
        purchaser_id=user.id
    )
    db.add(db_purchase)
    db.commit()
