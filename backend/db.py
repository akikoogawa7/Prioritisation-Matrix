from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData

engine = create_engine('postgresql://akikoogawa:password@localhost:5432/postgres')
meta = MetaData()
conn = engine.connect()
