from db import UserOrm, MatrixOutputORM, Session

local_session = Session()

user_to_delete = local_session.query(UserOrm).filter(UserOrm.username == 'akikoogawa7').first()

local_session.delete(user_to_delete)

local_session.commit()