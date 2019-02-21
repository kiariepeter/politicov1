import unittest

from app.tests.api.v2.office.OfficeBase import OfficeTest


class OfficeTests(OfficeTest):

    """Tests functionality of the political office endpoint"""

    def test_add_office(self):
        """Test API can create a office"""
        response = self.client().post('/api/v2/offices', data=self.add_office, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_all_office(self):
        """Tests API can get all offices"""
        response = self.client().get('/api/v2/offices')
        
        self.assertEqual(response.status_code, 200)

    def test_get_a_specific_office(self):
        """Tests API can get a specific office by using its id"""
        response = self.client().get('/api/v2/offices/1')
        self.assertEqual(response.status_code, 200)

    def test_update_office(self):
        """Update office tests"""
        response = self.client().patch('/api/v2/offices/1', data=self.add_update, content_type='application/json')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
