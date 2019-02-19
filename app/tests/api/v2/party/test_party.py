
import unittest

from app.tests.api.v2.party.Unitbase import PartTest

parties = []
class PartyTests(PartTest):
    """Tests functionality of the political endpoint"""

    def test_create_party(self):
        """Test API can create a party"""
        response = self.client().post('/api/v2/parties', data=self.add_party,
                                      content_type='application/json')

        # data = response.json['data'][0]['id']
        # parties.append(data)
        import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        """Tests API can get all parties"""
        response = self.client().get('/api/v2/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_a_specific_party_by_id(self):
        """Tests API can get a specific party by using its id"""

        response = self.client().get('/api/v2/parties/'+str(parties[0]), content_type='application/json')
        self.assertEqual(response.status_code, 200)

tear = PartTest()
tear.TearDown()
if __name__ == '__main__':
    unittest.main()
