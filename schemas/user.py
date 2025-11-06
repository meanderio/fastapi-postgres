from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserPublic(UserBase):
    id: int
