from db import Base, Session, engine
from uuid import uuid4
from sqlalchemy import Column, Integer, String, Table, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

class SessionORM(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    matrix_id = Column(ForeignKey('matrix.id'), primary_key=True)
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    # matrix = relationship("MatrixOutputORM", back_populates="creator")
    # user = relationship("UserORM", back_populates="matrix")

class UserORM(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    # matrix = relationship("SessionORM", back_populates="users")

    def __repr__(self):
        return f'<User username={self.username} email={self.email}>'

class MatrixORM(Base):
    __tablename__ = 'matrix'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(60), unique=True)
    description = Column(String(60))
    problem_statement = Column(String(60))
    # creator = relationship("SessionORM", back_populates="matrix")