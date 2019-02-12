
import unittest

from app.tests.api.v1.party.Unitbase import PartTest


class PartyTests(PartTest):
    """Tests functionality of the political endpoint"""

    def test_create_party(self):
        """Test API can create a party"""
        response = self.client().post('/api/v1/parties', data=self.add_party,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        """Tests API can get all parties"""
        response = self.client().get('/api/v1/parties')
        self.assertEqual(response.status_code, 201)

    def test_get_a_specific_party_by_id(self):
        """Tests API can get a specific party by using its id"""
        create_response = self.client().post('/api/v1/parties', data=self.add_party,
                                             content_type='application/json')

        if create_response:
            response = self.client().get('/api/v1/parties/1', content_type='application/json')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
