import json
from unittest import TestCase
from app import create_app


class OfficeTest(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # tear down tests

        self.add_office = json.dumps({
        "name": "Governor" ,
        "type":"federal"
        })

    def Tear_down(self):
        """Teardown tests"""
        self.app.testing = False
