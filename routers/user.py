import uuid
from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from db.database import get_db
from models.user import Users
from schemas.user import UserBase

router = APIRouter(prefix="/users", tags=["users"])


def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4)
    return session_id


@router.post("/create")
async def create_user(
    user: UserBase,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db),
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    db_user = Users(name=user.name)
    db.add(db_user)
    db.commit()


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
