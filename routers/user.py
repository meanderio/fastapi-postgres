from fastapi import APIRouter, Depends, HTTPException

# from schemas.user import UserBase
from sqlmodel import Session

# from sqlalchemy.orm import Session
from db.database import get_session
from models.user import Users

router = APIRouter(prefix="/users", tags=["users"])


# def get_session_id(session_id: Optional[str] = Cookie(None)):
#    if not session_id:
#        session_id = str(uuid.uuid4)
#    return session_id


@router.post("/create", response_model=Users)
async def create_user(
    user: Users,
    # response: Response,
    # session_id: str = Depends(get_session_id),
    session: Session = Depends(get_session),
):
    # response.set_cookie(key="session_id", value=session_id, httponly=True)
    # db_user = Users(name=user.name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/{user_id}", response_model=Users)
def get_user(user_id: int, session: Session = Depends(get_session)):
    # db_user = db.query(Users).filter(Users.id == user_id).first()
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
