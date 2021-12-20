from re import T
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import Column, Integer, String, Table, DateTime, create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()
meta = MetaData()

engine = create_engine("postgresql://postgres:password@localhost:5432/postgres", echo=True)

class SessionORM(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    matrix_id = Column(ForeignKey('matrix.id'), primary_key=True)
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    matrix = relationship("MatrixOutputORM", back_populates="creator")
    user = relationship("UserORM", back_populates="matrix")

class UserOrm(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(20), unique=True)
    email = Column(String(60), unique=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    matrix = relationship("Session", back_populates="users")

class MatrixOutputORM(Base):
    __tablename__ = 'matrix'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    creator = relationship("Session", back_populates="matrix")

Base.metadata.drop_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# user = UserOrm()
# user.id = 0
# user.username = 'akikoogawa'

# session.add(user)
# session.commit()
# session.close()