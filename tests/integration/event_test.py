from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel
import datetime


class EventTest(BaseTestCase):
    def test_events(self):
        with self.app_context():
            birth_date = datetime.date(1757, 1, 11)
            birth_event = EventModel(
                title='Birth of a Legend',
                description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
                date=birth_date)
            self.db_session.add(birth_event)
            self.db_session.commit()

            query = '''{ events { 
                        edges { 
                            node { 
                                title,
                                description,
                                date
                            } 
                        } 
                    } 
                }'''
            executed = self.client.execute(query)

            assert executed == {
                'data': {
                    'events': {
                        'edges': [
                            {
                                'node': {
                                    'title': 'Birth of a Legend',
                                    'description': 'Alexander Hamilton was born and spent part of his childhood in Charlestown.',
                                    'date': '1757-01-11T00:00:00'
                                }
                            }
                        ]
                    }
                }
            }
