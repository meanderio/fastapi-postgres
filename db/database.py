from sqlmodel import Session, SQLModel, create_engine

from core.config import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_tables():
    SQLModel.metadata.create_all(engine)
