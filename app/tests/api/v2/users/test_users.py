
from app.tests.api.v2.users.TestBase import TestUser

class UserTest(TestUser):
	"""docstring for UserTest"""

	def test_add_user(self):
		"""Test API can create a user"""
		response = self.client().post('/api/v2/users', data=self.register, content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_get_users(self):
		"""Test to get all users"""
		response = self.client().get('/api/v2/users')
		self.assertEqual(response.status_code, 201)
	def test_get_specific_user(self):
		"""Getting a specific user"""
		self.client().post('/api/v2/users', data=self.register, content_type='application/json')
		response = self.client().get('/api/v2/users/1')
		self.assertEqual(response.status_code, 201)
	def test_update_users(self):
		"""update users test"""
		response = self.client().patch('/api/v2/users/1', data = self.update, content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_login(self):
		"""test login ebdpoint"""
		response = self.client().post('/api/v2/login', data=self.login_data, content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_delete_user(self):
		"""Test to delete a specific user"""
		response = self.client().delete('/api/v2/users/1',content_type='application/json')
		self.assertEqual(response.status_code, 201)



if __name__ == "__main__":
	unittest.main()


