from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel


class EventMutationTest(BaseTestCase):
    @staticmethod
    def create_mock_event():
        return EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            occurred_on='1757-01-11')

    def test_create_event(self):
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

    def test_delete_event(self):
        with self.app_context():
            mock_event = EventMutationTest.create_mock_event()
            self.db_session.add(mock_event)
            self.db_session.commit()

            mutation = '''
            mutation deleteEvent {
                deleteEvent(input: {id: 1}) 
                {
                    status
                }
            }
            '''
            executed = self.client.execute(mutation)

            assert executed == {
                "data": {
                    "deleteEvent": {
                        "status": "ok"
                    }
                }
            }

    def test_delete_event_with_invalid_id_returns_error(self):
        with self.app_context():
            mutation = '''
            mutation deleteEvent {
                deleteEvent(input: {id: 1}) 
                {
                    status
                }
            }
            '''
            executed = self.client.execute(mutation)

            assert executed == {
                "data": {
                    "deleteEvent": {
                        "status": "event with ID 1 not found."
                    }
                }
            }
