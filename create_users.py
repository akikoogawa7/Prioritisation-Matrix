from db import UserOrm, Session

local_session = Session()

new_user = UserOrm(username='akikoogawa', email='akiko.ogawaa@gmail.com', first_name='Akiko', last_name='Ogawa')

local_session.add(new_user)
local_session.commit()