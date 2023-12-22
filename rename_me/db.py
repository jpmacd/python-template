import logging
from os import getenv
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

logging.basicConfig(
    format="[%(asctime)s][%(levelname)s][%(name)s:%(funcName)s:%(lineno)d] %(message)s",
)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)


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
