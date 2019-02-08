import json
from unittest import TestCase
from app.api.app import create_app



class PartTest(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # tear down tests

        self.add_party = json.dumps({
            "party_name": "Union Party",
            "logo": "http://app/logo.jpg",
            "members": "12"
        })

    def Tear_down(self):
        """Teardown tests"""
        self.app.testing = False
