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

	def create_user(self,users):
		"""This method saves user data in the database"""
		try:
			cur.execute("INSERT INTO tbl_users(firstname,lastname,othername,phoneNumber,passportUrl,email,password) VALUES(%s ,%s ,%s, %s, %s, %s, %s)", (users[0],users[1],users[2],users[3],users[4],users[5],users[6]))
			cur.execute("SELECT * FROM tbl_users where status=1 order by id desc")
			users = cur.fetchall()
			return make_response(jsonify({'status':201,'message':'user added successfully','data':users}),201)
		except psycopg2.DatabaseError as e:
			print(e)
			return make_response(jsonify({'status':409,'message':"failed to save data "+str(e.args[0]) }), 409)

	def get_users(self):
		"""querying the database to get all users"""
		cur.execute("SELECT * FROM tbl_users  order by id desc")
		rows = cur.fetchall()
		return make_response(jsonify({'status':201,'data':rows}),201)
	def get_userByid(self,user_id):
		"""This method returns a specific user by id"""
		cur.execute("SELECT * FROM tbl_users where  id = %s",(str(user_id)))
		row = cur.fetchall()
		size =len(row)
		if  size > 0:
			return make_response(jsonify({'status':201, 'data': row}), 201)
		return make_response(jsonify({'status':404, 'message': 'user not found'}),404)
	@staticmethod
	def login(email,password):
		"""This method validates user credentials"""
		cur.execute("SELECT * FROM tbl_users where  email = %s and password = %s" ,(email,password))
		row = cur.fetchall()
		size =len(row)
		if  size > 0:
			token = jwt.encode({'user':row[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, MY_APIKEY)
			return make_response(jsonify({'status':201,"message":"logged in successfully", 'token':token.decode('UTF-8')}),201)
		return make_response(jsonify({'status':404,"message":"invalid user"}))

	def update_user(self,user_id,user_data):
		"""This method updates specific user details"""
		cur.execute("SELECT * FROM tbl_users where  id = %s",(str(user_id)))
		row = cur.fetchall()
		size =len(row)
		if  size > 0:
			cur.execute("UPDATE tbl_users set name= %s,email= %s,phone = %s,photo = %s,national_id= %s WHERE id = %s",(user_data['name'],user_data['email'], user_data['phone'],user_data['photo'],user_data['national_id'],str(user_id)))
			return make_response(jsonify({'status':201, 'message': "user updated successfully"}), 201)
		return make_response(jsonify({'status':404, 'message': 'user not found'}),404)
	def delete_user(self,user_id):
		"""This method deletes specific user by id"""
		cur.execute("SELECT * FROM tbl_users where  id = %s",(str(user_id)))
		row = cur.fetchall()
		size =len(row)
		if  size > 0:
			cur.execute("DELETE  FROM  tbl_users  WHERE id = %s",(str(user_id)))
			return make_response(jsonify({'status':201, 'message': "user deleted successfully"}), 201)
		return make_response(jsonify({'status':404, 'message': 'user not found'}),404)

		


		


