from models import UserORM, MatrixORM
from db import Session

local_session = Session()

user_to_delete = local_session.query(UserORM).filter(UserORM.username == 'akikoogawa7').first()

local_session.delete(user_to_delete)

local_session.commit()