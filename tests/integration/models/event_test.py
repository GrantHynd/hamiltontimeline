from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel


class EventTest(BaseTestCase):
    @staticmethod
    def create_mock_event():
        return EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            occurred_on='1757-01-11')

    def test_crud(self):
        with self.app_context():
            mock_event = EventTest.create_mock_event()
            self.assertIsNone(EventModel.find_by_id(mock_event.id))
            mock_event.save_to_db()
            self.assertIsNotNone(EventModel.find_by_id(mock_event.id))
            mock_event.delete_from_db()
            self.assertIsNone(EventModel.find_by_id(mock_event.id))
