from fastapi import APIRouter, Depends, HTTPException, Response

# from schemas.purchase import PurchaseBase
from sqlmodel import Session

# from sqlalchemy.orm import Session
from db.database import get_session
from models.purchase import Purchases

router = APIRouter(prefix="/purchases", tags=["purchases"])


# def get_session_id(session_id: Optional[str] = Cookie(None)):
#    if not session_id:
#        session_id = str(uuid.uuid4)
#    return session_id


@router.post("/create", response_model=Purchases)
async def create_purchase(
    purchase: Purchases,
    response: Response,
    # session_id: str = Depends(get_session_id),
    session: Session = Depends(get_session),
):
    # response.set_cookie(key="session_id", value=session_id, httponly=True)
    # user = db.query(Users).filter(Users.name == purchase.name).first()
    # db_purchase = Purchases(
    #    location=purchase.location, amount=purchase.amount, purchaser_id=user.id
    # )
    session.add(purchase)
    session.commit()
    session.refresh(purchase)
    return purchase


@router.get("/{purchase_id}", response_model=Purchases)
def get_purchase(purchase_id: int, session: Session = Depends(get_session)):
    purchase = session.get(Purchases, purchase_id)
    # print(db_purchase.purchaser.name, dir(db_purchase.purchaser))
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase
