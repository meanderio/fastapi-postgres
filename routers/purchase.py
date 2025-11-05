import uuid
from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from db.database import get_db
from models.purchase import Purchases
from models.user import Users
from schemas.purchase import PurchaseBase

router = APIRouter(prefix="/purchases", tags=["purchases"])


def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4)
    return session_id


@router.post("/create")
async def create_user(
    purchase: PurchaseBase,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db),
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    user = db.query(Users).filter(Users.name == purchase.name).first()
    db_purchase = Purchases(
        location=purchase.location, amount=purchase.amount, purchaser_id=user.id
    )
    db.add(db_purchase)
    db.commit()


@router.get("/{purchase_id}")
def get_user(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = db.query(Purchases).filter(Purchases.id == purchase_id).first()
    if not db_purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase
