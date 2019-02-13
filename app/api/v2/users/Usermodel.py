from flask import make_response,jsonify
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

	def create_user(self,name,email,phone,photo,password):
		user_id = len(users) + 1
		new_users = {'user_id':user_id,
					'name':name,
					'email':email,
					'phone':phone,
					'photo':photo,
					'password':password,
					'user_type':2,
					'status':1}
		users[user_id] = new_users

	def get_users(self):
		return self.users
	@staticmethod
	def login(email,password):
		for x in users.values():
			if x['email'] == email and x['password'] == password:
				return make_response(jsonify({'status':201,"message":"logged in successfully"}),201)
		return make_response(jsonify({'status':404,"message":"invalid user"}))


		


