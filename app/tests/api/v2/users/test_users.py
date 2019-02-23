from app.tests.api.v2.users.TestBase import TestUser
import json
import psycopg2.extras
from unittest import TestCase
from connection import connect
from schema import start_db
import json

conn = connect()

cur: object = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

users = []
token = []

class UserTest(TestUser):
    """docstring for UserTest"""

    def test_weak_password(self):
        response = self.client().post('/api/v2/auth/signup', data=self.weak_password, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_has_small_letters(self):
        response = self.client().post('/api/v2/auth/signup', data=self.has_small_letters,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_has_special_character(self):
        response = self.client().post('/api/v2/auth/signup', data=self.has_small_letters,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_has_caps_letters(self):
        response = self.client().post('/api/v2/auth/signup', data=self.has_caps_letters,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_sign_up(self):
        """Test API can create a user"""
        response = self.client().post('/api/v2/auth/signup', data=self.register, content_type='application/json')
        # import pdb;pdb.set_trace()
        user_id = response.json["data"]["id"]
        tokens = response.json["data"]["token"]
        users.append(user_id)
        token.append(tokens)
        self.assertEqual(response.status_code, 201)

    #
    def test_get_users(self):
        """Test to get all users"""
        header = {"x-access-token:"+token[0]}
        response = self.client().get('/api/v2/users', headers=header)
        self.assertEqual(response.status_code, 201)

    # def test_get_specific_user(self):
    # 	"""Getting a specific user"""
    # 	response = self.client().get('/api/v2/users/'+str(users[0]))
    # 	self.assertEqual(response.status_code, 200)
    # def test_update_users(self):
    # 	"""update users test"""
    # 	response = self.client().patch('/api/v2/users/'+str(users[0]), data = self.update, content_type='application/json')
    # 	self.assertEqual(response.status_code, 200)
    #
    # def test_login(self):
    # 	"""test login ebdpoint"""
    # 	response = self.client().post('/api/v2/login', data=self.login_data, content_type='application/json')
    # 	self.assertEqual(response.status_code, 200)
    #
    # def test_delete_user(self):
    # 	"""Test to delete a specific user"""
    # 	info = self.client().post('/api/v2/auth/signup', data=self.update, content_type='application/json')
    # 	user_id = info.json['data'][0]['id']
    #
    # 	response = self.client().delete('/api/v2/users/'+str(user_id),content_type='application/json')
    # 	self.assertEqual(response.status_code, 200)

    def teardown(self):
        cur.execute("""DROP TABLE IF EXISTS tbl_users CASCADE""")


if __name__ == "__main__":
    unittest.main()
