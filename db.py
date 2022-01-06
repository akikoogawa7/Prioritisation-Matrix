from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from fastapi import Depends
from schemas import Matrix


Base = declarative_base()
meta = MetaData()

POSTGRESQL_DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

engine = create_engine(POSTGRESQL_DATABASE_URL, echo=True)

Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)

# Database dependency
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

# session = Session()

# session.add(user)
# session.commit()
# session.close()
