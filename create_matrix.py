from db import MatrixOutputORM, Session

local_session = Session()

new_matrix = MatrixOutputORM(public_key='1234', name='matrix 1')

local_session.add(new_matrix)
local_session.commit()