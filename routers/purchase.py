from fastapi import APIRouter, HTTPException, Response
from sqlmodel import Session

from db.database import SessionDep
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
    session: Session = SessionDep,
):
    # response.set_cookie(key="session_id", value=session_id, httponly=True)
    session.add(purchase)
    session.commit()
    session.refresh(purchase)
    return purchase


@router.get("/{purchase_id}", response_model=Purchases)
def get_purchase(purchase_id: int, session: Session = SessionDep):
    purchase = session.get(Purchases, purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase
