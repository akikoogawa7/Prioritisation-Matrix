from db import Session, UserOrm, MatrixOutputORM

local_session = Session()

# returns all data
users = local_session.query(UserOrm).all()
matrices = local_session.query(MatrixOutputORM).all()[:3] # limits to 3

for user in users:
    print(user.username)