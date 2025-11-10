from fastapi import APIRouter, HTTPException
from sqlmodel import Session

from db.database import SessionDep
from models.user import User, UserCreate, UserPublic, UserPublicWithPurchases

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: Session = SessionDep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserPublicWithPurchases)
def get_user(user_id: int, session: Session = SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# @router.get("/", response_model=list[Users])
# async def get_users(session: Session = SessionDep, offset: int = 0, limit: int = 100):
#    users = session.exec(select(Users).offset(offset).limit(limit)).all()
#    return users
