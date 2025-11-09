from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from db.database import SessionDep
from models.user import User, UserCreate, UserPublic

router = APIRouter(prefix="/users", tags=["users"])


# def get_session_id(session_id: Optional[str] = Cookie(None)):
#    if not session_id:
#        session_id = str(uuid.uuid4)
#    return session_id
@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: Session = SessionDep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

#@router.post("/create", response_model=Users)
#async def create_user(
#    user: Users,
#    # response: Response,
#    # session_id: str = Depends(get_session_id),
#    session: Session = SessionDep,
#) -> Users:
#    # response.set_cookie(key="session_id", value=session_id, httponly=True)
#    session.add(user)
#    session.commit()
#    session.refresh(user)
#    return user


#@router.get("/", response_model=list[Users])
#async def get_users(session: Session = SessionDep, offset: int = 0, limit: int = 100):
#    users = session.exec(select(Users).offset(offset).limit(limit)).all()
#    return users
#
#
#@router.get("/{user_id}", response_model=Users)
#async def get_user(user_id: int, session: Session = SessionDep) -> Users:
#    user = session.get(Users, user_id)
#    if not user:
#        raise HTTPException(status_code=404, detail="User not found")
#    return user
