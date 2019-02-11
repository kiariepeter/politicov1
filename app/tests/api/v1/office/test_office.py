import unittest

from app.tests.api.v1.office.OfficeBase import OfficeTest


class OfficeTests(OfficeTest):
    """Tests functionality of the political office endpoint"""

    def test_office_party(self):
        """Test API can create a office"""
        response = self.client().post('/api/v1/add_office', data=self.add_office, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_office(self):
        """Tests API can get all offices"""
        response = self.client().get('/api/v1/get_offices')
        self.assertEqual(response.status_code, 201)

    def test_get_a_specific_office_by_id(self):
        """Tests API can get a specific office by using its id"""
        create_response = self.client().post('/api/v1/add_office', data=self.add_office,
                                             content_type='application/json')
        if create_response:
            response = self.client().get('/api/v1/get_offices')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
