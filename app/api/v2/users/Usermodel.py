from flask import make_response,jsonify
import psycopg2
import psycopg2.extras
from connection import connect
import json
import jwt
import datetime

MY_APIKEY = 'hj5499GFWDRWw988ek<MKL(IEI$NMR'


conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
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

	def create_user(self,users):
		"""This method saves user data in the database"""
		try:
			cur.execute("INSERT INTO tbl_users(name,email,phone,photo,password,national_id) VALUES(%s ,%s ,%s, %s, %s, %s)", (users[0],users[1],users[2],users[3],users[4],users[5]))
			return make_response(jsonify({'status':201,'message':'user added successfully','users':users}),201)
		except psycopg2.DatabaseError as e:
			print(e)
			return make_response(jsonify({'status':409,'message':"failed to save data "+str(e.args[0]) }), 409)



	def get_users(self):
		"""querying the database to get all users"""
		cur.execute("SELECT * FROM tbl_users")
		rows = cur.fetchall()
		return make_response(jsonify({'status':201,'users':rows}),201)
	def get_userByid(self,user_id):
		cur.execute("SELECT * FROM tbl_users where id = %s",(str(user_id)))
		row = cur.fetchall()
		size =len(row)
		if  size > 0:
			return make_response(jsonify({'status':201, 'user': row}), 201)
		return make_response(jsonify({'status':404, 'message': 'user not found'}),404)
	@staticmethod
	def login(email,password):
		for x in users.values():
			if x['email'] == email and x['password'] == password:
				token = jwt.encode({'user':x['name'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, MY_APIKEY)
				return make_response(jsonify({'status':201,"message":"logged in successfully", 'token':token.decode('UTF-8')}),201)
		return make_response(jsonify({'status':404,"message":"invalid user"}))


		


