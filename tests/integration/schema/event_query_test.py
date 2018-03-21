from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel


class EventQueryTest(BaseTestCase):
    @staticmethod
    def create_mock_event():
        return EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            occurred_on='1757-01-11')

    def test_events_query(self):
        with self.app_context():
            mock_event = EventQueryTest.create_mock_event()
            self.db_session.add(mock_event)
            self.db_session.commit()

            query = '''{ events { 
                        edges { 
                            node { 
                                title,
                                description,
                                occurredOn
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
                                    'occurredOn': '1757-01-11T00:00:00'
                                }
                            }
                        ]
                    }
                }
            }
