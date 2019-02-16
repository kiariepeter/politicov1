from flask import make_response,jsonify
from connection import connect
import json
import jwt
import datetime

MY_APIKEY = 'hj5499GFWDRWw988ek<MKL(IEI$NMR'


conn = connect()
cur = conn.cursor()
users = {}




class User(object):
	"""user class for User"""
	def __init__(self):
		self.user_id = 0
		self.name = ''
		self.email = ''
		self.phone ='',
		self.photo = ''
		self.password =''
		self.user_type = 0
		self.status = 1
		self.users = users

	def create_user(self,name,email,phone,photo,password,national_id):
		user_id = len(users) + 1
		user_type = '2'
		status ='1'

		try:
			cur.execute("INSERT INTO users(name,email,phone,national_id,photo,user_type,status) VALUES(%s ,%s ,%s, %s, %s, %s,%s )", (name,email,phone,national_id,photo,user_type,status))
		except (Exception, psycopg2.DatabaseError )as e:
			print(e)



	def get_users(self):
		"""querying the database to get all users"""
		cur.execute("SELECT * FROM users")
		rows = cur.fetchall()
		return jsonify(rows)
	@staticmethod
	def login(email,password):
		for x in users.values():
			if x['email'] == email and x['password'] == password:
				token = jwt.encode({'user':x['name'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, MY_APIKEY)
				return make_response(jsonify({'status':201,"message":"logged in successfully", 'token':token.decode('UTF-8')}),201)
		return make_response(jsonify({'status':404,"message":"invalid user"}))


		


