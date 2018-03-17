"""
BaseTestCase

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from sqlalchemy import *
from unittest import TestCase
from config import config
from app import app
from database.db import engine, db_session, Base
from schema import schema
from graphene.test import Client


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
        app.config['DEBUG'] = config['DEBUG']
        app.config['PROPAGATE_EXCEPTIONS'] = config['PROPAGATE_EXCEPTIONS']

    def setUp(self):
        with app.app_context():
            Base.metadata.create_all(bind=engine)
        self.app = app.test_client
        self.app_context = app.app_context
        self.db_session = db_session
        self.schema = schema
        self.client = Client(self.schema)

    def tearDown(self):
        # Database is blank
        with app.app_context():
            self.db_session.remove()
            Base.metadata.drop_all(bind=engine)
