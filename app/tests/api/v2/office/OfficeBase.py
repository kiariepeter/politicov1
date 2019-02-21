import json
from unittest import TestCase
from app import create_app
import psycopg2
import psycopg2.extras
from connection import connect
conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


class OfficeTest(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # tear down tests

        self.add_office = json.dumps({
        "name": "Goverhgjhgjnor" ,
        "type":"federal"
        })

        self.add_update = json.dumps({
        "name": "Governpor" ,
        "type":"federal"
        })

    def Tear_down(self):
        """Teardown tests"""
        self.app.testing = False
        
