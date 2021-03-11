from config import LOGIN, PASSWORD, HOST, PORT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_NAME = "me_db"

engine = create_engine(f'postgres://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()