from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel


class EventTest(BaseTestCase):

    @staticmethod
    def create_mock_event():
        return EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            occurred_on='1757-01-11')

    def test_events_query(self):
        with self.app_context():
            mock_event = EventTest.create_mock_event()
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

    def test_create_event(self):
        with self.app_context():
            mock_event = EventTest.create_mock_event()
            mock_event.save_to_db()
            queried_event = EventModel.query.filter(EventModel.title == 'Birth of a Legend').first()

            self.assertEqual('Birth of a Legend', queried_event.title)
            self.assertEqual('Alexander Hamilton was born and spent part of his childhood in Charlestown.', queried_event.description)
            self.assertEqual('Tue Jan 11 00:00:00 1757', queried_event.occurred_on.ctime())

    def test_create_event_mutation(self):
        with self.app_context():
            mutation = '''
            mutation createEvent {
                createEvent(input: 
                {
                    title: "The birth of Alexander",
                    description: "A great event",
                    occurredOn: "1757-01-11"
                }) 
                {
                    event 
                    {
                        title
                        description
                        occurredOn
                    }
                }
            }
            '''
            executed = self.client.execute(mutation)

            assert executed == {
                "data": {
                    "createEvent": {
                        "event": {
                            "title": "The birth of Alexander",
                            "description": "A great event",
                            "occurredOn": "1757-01-11T00:00:00"
                        }
                    }
                }
            }