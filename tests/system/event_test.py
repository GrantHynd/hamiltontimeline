from tests.base_test_case import BaseTestCase
from models.event import Event as EventModel
import json


class EventTest(BaseTestCase):
    def test_create_event(self):
        with self.app() as client:
            create_event_mutation = {
                "query": "mutation createEvent($event: CreateEventInput!) { createEvent(input: $event) { event { title description occurredOn } } }",
                "operationName": "createEvent",
                "variables": {
                    "event": {
                        "title": "Birth of a Legend",
                        "description": "Alexander Hamilton was born and spent part of his childhood in Charlestown.",
                        "occurredOn": "1757-01-11"
                    }
                }
            }

            response = client.post('/graphql',
                                   data=json.dumps(create_event_mutation),
                                   headers={'Content-Type': 'application/json'})

            self.assertEqual(EventModel.find_by_id(1).title, "Birth of a Legend")
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(json.loads(response.data),
                                 {
                                     "data": {
                                         "createEvent": {
                                             "event": {
                                                 "title": "Birth of a Legend",
                                                 "description": "Alexander Hamilton was born and spent part of his childhood in Charlestown.",
                                                 "occurredOn": "1757-01-11T00:00:00"
                                             }
                                         }
                                     }
                                 })

    def test_create_event_with_empty_title(self):
        with self.app() as client:
            create_event_mutation = {
                "query": "mutation createEvent($event: CreateEventInput!) { createEvent(input: $event) { event { title description occurredOn } } }",
                "operationName": "createEvent",
                "variables": {
                    "event": {
                        "title": "",
                        "description": "Alexander Hamilton was born and spent part of his childhood in Charlestown.",
                        "occurredOn": "1757-01-11"
                    }
                }
            }

            response = client.post('/graphql',
                                   data=json.dumps(create_event_mutation),
                                   headers={'Content-Type': 'application/json'})

            self.assertIsNone(EventModel.find_by_id(1))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)['data'], {"createEvent": {"event": None}})
            self.assertEqual(json.loads(response.data)['errors'][0]['message'], 'Title must not be blank')