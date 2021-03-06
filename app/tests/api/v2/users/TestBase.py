from app import create_app
import psycopg2
import psycopg2.extras
from unittest import TestCase
from connection import connect
from schema import start_db
import json
conn = connect()
# import pdb;pdb.set_trace()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


class TestUser(TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client
		self.start_db = start_db()
		self.user_data = []

		self.register = json.dumps({
		"firstname":"PETER",
		"lastname":"Kish",
		"othername":"dsds",
		"passportUrl":"http://www.politioc.com/photo.jpg",
		"email":"peteteer@gmail.com",
		"phoneNumber":"08487434",
		"password":"123456A@h"
		})
		self.weak_password = json.dumps({
		"firstname":"PETER",
		"phoneNumber":"074354443",
		"lastname":"Kish",
		"othername":"dsds",
		"passportUrl":"http://www.politioc.com/photo.jpg",
		"email":"kqjwrwaqqqie2wawpeter4@gmail.com",
		"password":"1234"
		})
		self.has_caps_letters = json.dumps({
		"firstname":"PETER",
		"phoneNumber":"074354443",
		"lastname":"Kish",
		"othername":"dsds",
		"passportUrl":"http://www.politioc.com/photo.jpg",
		"email":"k@gmail.com",
		"password":"123456wer"
		})
		self.has_small_letters = json.dumps({
		"firstname":"PETER",
		"phoneNumber":"074354443",
		"lastname":"Kish",
		"othername":"dsds",
		"passportUrl":"http://www.politioc.com/photo.jpg",
		"email":"k@gmail.com",
		"password":"123456AWE"
		})

		
		self.update = json.dumps({
		"firstname":"PETER",
		"phoneNumber":"07434436776",
		"lastname":"Kish",
		"othername":"dsds",
		"passportUrl":"http://www.politioc.com/photo.jpg",
		"email":"kwwiahrie2peter4@gmail.com",
		"password":"1234"
		})

		self.login_data = json.dumps({
		"email":"kiarie2peter4@gmail.com",
		"password":"1234"
		})

	def tearDown(self):
		tear_users ="""TRUNCATE tbl_users CASCADE"""
		cur.execute(tear_users)



		