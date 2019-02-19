
from app.tests.api.v2.users.TestBase import TestUser
import json

users = []
class UserTest(TestUser):
	"""docstring for UserTest"""

	def test_add_user(self):
		"""Test API can create a user"""
		response = self.client().post('/api/v2/auth/signup', data=self.register, content_type='application/json')
		data = response.json['data'][0]['id']
		users.append(data)
		self.assertEqual(response.status_code, 201)


	def test_get_users(self):
		"""Test to get all users"""
		response = self.client().get('/api/v2/users')
		self.assertEqual(response.status_code, 201)
	def test_get_specific_user(self):
		"""Getting a specific user"""
		response = self.client().get('/api/v2/users/'+str(users[0]))
		self.assertEqual(response.status_code, 200)
	def test_update_users(self):
		"""update users test"""
		response = self.client().patch('/api/v2/users/'+str(users[0]), data = self.update, content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_login(self):
		"""test login ebdpoint"""
		response = self.client().post('/api/v2/login', data=self.login_data, content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_delete_user(self):
		"""Test to delete a specific user"""
		info = self.client().post('/api/v2/auth/signup', data=self.update, content_type='application/json')
		user_id = info.json['data'][0]['id']
		
		response = self.client().delete('/api/v2/users/'+str(user_id),content_type='application/json')
		self.assertEqual(response.status_code, 200)



tear = TestUser()
tear.TearDown()

if __name__ == "__main__":
	unittest.main()


