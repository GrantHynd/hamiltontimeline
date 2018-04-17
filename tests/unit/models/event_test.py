from tests.unit.unit_test_case import UnitTestCase
from models.event import Event as EventModel


class EventTest(UnitTestCase):
    def test_event_model(self):
        birth_event = EventModel(
            title='Birth of a Legend',
            description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
            occurred_on='1757-01-11')

        self.assertEqual('Birth of a Legend', birth_event.title)
        self.assertEqual('Alexander Hamilton was born and spent part of his childhood in Charlestown.', birth_event.description)
        self.assertEqual('Tue Jan 11 00:00:00 1757', birth_event.occurred_on.ctime())

    def test_event_model_with_blank_values(self):
        with self.assertRaises(ValueError):
            EventModel(
                title='',
                description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
                occurred_on='1757-01-11')

        with self.assertRaises(ValueError):
            EventModel(
                title='Birth of a Legend',
                description='',
                occurred_on='1757-01-11')

        with self.assertRaises(ValueError):
            EventModel(
                title='',
                description='Alexander Hamilton was born and spent part of his childhood in Charlestown.',
                occurred_on='')
