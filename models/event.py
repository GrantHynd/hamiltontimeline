from sqlalchemy import *
from database.db import Base, db_session
from datetime import datetime


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    occurred_on = Column(DateTime)

    def __init__(self, title, description, occurred_on):
        self.title = title
        self.description = description
        self.occurred_on = datetime.strptime(occurred_on, '%Y-%m-%d')

    def set_occurred_on(self, occurred_on):
        self.occurred_on = datetime.strptime(occurred_on, '%Y-%m-%d')

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()

    def delete_from_db(self):
        db_session.delete(self)
        db_session.commit()
