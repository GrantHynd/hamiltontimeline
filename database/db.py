from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config

engine = create_engine(config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def db_init():
    Base.metadata.create_all(bind=engine)


def db_drop():
    Base.metadata.drop_all(bind=engine)

