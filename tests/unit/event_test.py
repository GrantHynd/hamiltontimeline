from tests.unit.unit_test_case import UnitTestCase
from models.event import Event as EventModel
from datetime import date


class EventTest(UnitTestCase):
    def test_event_model(self):
        birth_date = date(1757, 1, 11)
        birth_event = EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            date=birth_date)

        self.assertEqual('Birth of a Legend', birth_event.title)
        self.assertEqual('Alexander Hamilton was born and spent part of his childhood in Charlestown.', birth_event.description)
        self.assertEqual('Tue Jan 11 00:00:00 1757', birth_event.date.ctime())
