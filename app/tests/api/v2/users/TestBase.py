from app import create_app
from unittest import TestCase
import json

class TestUser(TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client

		self.register = json.dumps({
		"name":"PETER KIARIE",
		"phone":"0720068822",
		"photo":"http://www.politioc.com/photo.jpg",
		"email":"kiarie2peter4@gmail.com",
		"national_id":"124",
		"password":"1234"
		})
		self.update = json.dumps({
		"name":"Kimento james",
		"phone":"073434544",
		"photo":"http://www.politioc.com/photo.jpg",
		"email":"kipeter4@gmail.com",
		"national_id":"1257654",
		"password":"123789894"
		})

		self.login_data = json.dumps({
		"email":"kiarie2peter4@gmail.com",
		"password":"1234"
		})

	def TearDown(self):
		self.app.testing = False