from fastapi import APIRouter, HTTPException
from sqlmodel import Session

from db.database import SessionDep
from models.purchase import (
    Purchase,
    PurchaseCreate,
    PurchasePublic,
    PurchasePublicWithUser,
)

router = APIRouter(prefix="/purchases", tags=["purchases"])


@router.post("/", response_model=PurchasePublic)
def create_purchase(purchase: PurchaseCreate, session: SessionDep = SessionDep):
    db_purchase = Purchase.model_validate(purchase)
    session.add(db_purchase)
    session.commit()
    session.refresh(db_purchase)
    return db_purchase


@router.get("/{purchase_id}", response_model=PurchasePublicWithUser)
def get_purchase(purchase_id: int, session: Session = SessionDep):
    purchase = session.get(Purchase, purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase
