from os import getenv
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


class Root(Base):
    __tablename__ = "root"
    id = Column(Integer, primary_key=True)


engine = create_engine(
    f'{getenv("DB_URL")}',
    echo=False,
    echo_pool=False,
    pool_size=getenv("SQLALCHEMY_POOL_SIZE", "25"),
    max_overflow=getenv("SQLALCHEMY_MAX_OVERFLOW", "50"),
)


def get_db_session():
    session = sessionmaker(bind=engine)
    return session()


Base.metadata.create_all(engine)
