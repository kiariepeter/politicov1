from flask import request, jsonify, Blueprint, make_response
from app.api.v2.users.Usermodel import User, users

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/users',methods = ['POST'])
def add_user():
	"""Given that am a new user i should be able to register"""
	try:
		if not request.get_json():
			return make_response(jsonify({'status':404 , 'message':'missing input'}),404)
		post_data = request.get_json()
		name =  post_data['name']
		phone =  post_data['phone']
		email =  post_data['email']
		photo =  post_data['photo']
		password = post_data['password']
		for x in users.values():
			if x['email'] == email:
				return make_response(jsonify({'status':203,"message":"user with the same email already exists"}),203)
		user = User()
		user.create_user(name,email,phone,photo,password)
		return make_response(jsonify({'status':201,'message':'user added successfully','users':users}),201)
	except Exception as e:
		return make_response(jsonify({'status':400 ,'message':'bad request'}))

@user_blueprint.route('/users',methods = ['GET'])
def get_all_users():
	"""Given that i am an admin i should view all rgistered users"""
	if users:
		return make_response(jsonify({'status':201,'users':users}),201)
	return make_response(jsonify({'status':404,'message':'no users found'}),404)

@user_blueprint.route('/users/<int:user_id>',methods = ['GET'])
def get_user(user_id):
	"""Given that i am an admin i should be able to view a specific user details"""
	if user_id in users:
		return make_response(jsonify({'status':201, 'user': users.get(user_id) }))
	return make_response(jsonify({'status':404, 'message':'user not found'}))

@user_blueprint.route('/users/<int:user_id>',methods =['PATCH'])
def update_user(user_id):
	"""Given that i am an admin i should update specific user details """
	if user_id:
		if not request.get_json():
			return make_response(jsonify({'status':400,'message': 'Post data missing'}),400)
		if user_id not in users:
			return make_response(jsonify({'status':404,'message': 'user not found'}),404)
		post_data = request.get_json()
		users[user_id]['name'] =  post_data['name']
		users[user_id]['phone'] =  post_data['phone']
		users[user_id]['email'] =  post_data['email']
		users[user_id]['photo'] =  post_data['photo']
		return make_response(jsonify({'status':201,'users': users}),201)

@user_blueprint.route('/users/<int:user_id>',methods = ['DELETE'])
def delete_user(user_id):
	"""Given that i am an admin i should be able to delete a specific user"""
	if user_id:
		if user_id in users:
			del users[user_id]
			return make_response(jsonify({'status':201,'message':'user deleted successfully','users':users}),201)

@user_blueprint.route('login',methods =['POST'])
def login():
	if not request.get_json():
		return make_response(jsonify({"status":409,"message":"missing post data"}))
	post_data = request.get_json()
	users = User()
	res = users.login(post_data['email'],post_data['password'])
	return res



