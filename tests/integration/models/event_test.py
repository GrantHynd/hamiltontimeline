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
            # Create event and assert that it is not in the database
            mock_event = EventTest.create_mock_event()
            self.assertIsNone(EventModel.find_by_id(mock_event.id))

            # Save event to database and assert that it is in the database
            mock_event.save_to_db()
            self.assertIsNotNone(EventModel.find_by_id(mock_event.id))

            # Update event details and save to database then assert that details have been updated
            mock_event.title = "Updated title"
            mock_event.description = "Updated description"
            mock_event.set_occurred_on("1755-01-11")
            mock_event.save_to_db()
            updated_mock_event = EventModel.find_by_id(mock_event.id)
            self.assertEqual("Updated title", updated_mock_event.title)
            self.assertEqual("Updated description", updated_mock_event.description)
            self.assertEqual("Sat Jan 11 00:00:00 1755", updated_mock_event.occurred_on.ctime())

            # Delete event from database and assert event is no longer in database
            updated_mock_event.delete_from_db()
            self.assertIsNone(EventModel.find_by_id(updated_mock_event.id))
