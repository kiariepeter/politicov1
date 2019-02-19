from app import create_app
import psycopg2
import psycopg2.extras
from unittest import TestCase
from connection import connect
from schema import start_db
import json
conn = connect()
# import pdb;pdb.set_trace()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


class PartTest(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.start_db = start_db()
        # tear down tests
        self.add_party = json.dumps({
        "name": "new pwearty",
        "logoUrl":"http://www.politico.com/logo.jpg",
        "hqAddress":"Po Box 456 Nairobi",
        "slogan":"pamojava"
        })

    def TearDown(self):
        """Teardown tests"""
        tear_party ="""DROP TABLE IF EXISTS tbl_parties CASCADE"""
        cur.execute(tear_party)
