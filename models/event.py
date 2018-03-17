from sqlalchemy import *
from database.db import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    date = Column(DateTime)
