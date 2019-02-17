from flask import request, jsonify, Blueprint, make_response
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app.api.v2.users.Usermodel import User, users
import jwt
from functools import wraps
import datetime
import json
from custom_validator import My_validator as validate

MY_APIKEY = 'hj5499GFWDRWw988ek<MKL(IEI$NMR'
user_blueprint = Blueprint('users', __name__)


def tokenizer(f):
	@wraps(f)
	def my_wrapper(*args, **kwargs):

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return make_response(jsonify({'status':404, 'message':'token is missing'}), 404)
		try:
			data = jwt.decode(token, MY_APIKEY)
		except Exception as e:
			return make_response(jsonify({'status':400, 'message':'invalid token passed'}),400)

		return f(*args, **kwargs)
	return my_wrapper




@user_blueprint.route('/users',methods = ['POST'])
def add_user():
	"""Given that am a new user i should be able to register"""
	errors = []
	try:
		if not request.get_json():
			error.append(make_response(jsonify({'status':404 , 'message':'missing input'}),404))
		post_data = request.get_json()
		check_missingfields= validate.missing_value_validator(['name','phone','email','photo','password','national_id'],post_data)
		if  check_missingfields !=True:errors.append(check_missingfields)
		check_emptyfield = validate.empty_string_validator(['name','phone','email','photo','password'],post_data)
		if check_emptyfield !=True:errors.append(check_emptyfield)
		name =  post_data['name']
		phone =  post_data['phone']
		email =  post_data['email']
		photo =  post_data['photo']
		password = post_data['password']
		national_id = post_data['national_id']
		check_if_integer = validate.is_integer_validator(['national_id'],post_data)
		if check_if_integer !=True:errors.append(check_if_integer)
		check_if_validurl = validate.is_valid_url(photo)
		if check_if_validurl !=True:errors.append(check_if_validurl)
		check_if_valid_email = validate.is_validEmail(email)
		if check_if_valid_email !=True:errors.append(check_if_valid_email)
		check_if_text_only = validate.is_text_only(name)
		if check_if_text_only !=True:errors.append(check_if_text_only)
		for x in users.values():
			if x['email'] == email and x['national_id'] == national_id:
				 error.append(make_response(jsonify({'status':203,"message":"user with the same details already exists"}),203))
		if len(errors) > 0:
			for e in errors:
				return e
		user = User()
		res = user.create_user([name,email,phone,photo,password,national_id])
		return res
	except KeyError as e:
		return make_response(jsonify({'status':400 ,'message':'bad request'}), 400)




@user_blueprint.route('/users',methods = ['GET'])
@tokenizer
def get_all_users():
	"""Given that i am an admin i should view all registered users"""
	user = User()
	all_users = user.get_users()
	if all_users:
		return make_response(all_users,201)
	return make_response(jsonify({'status':404,'message':'no users found'}),404)

@user_blueprint.route('/users/<int:user_id>',methods = ['GET'])
@tokenizer
def get_user(user_id):
	"""Given that i am an admin i should be able to view a specific user details"""
	user = User()
	if user_id:
		check_if_integer = validate.is_single_integer(user_id)
		if check_if_integer !=True:return check_if_integer
		res = user.get_userByid(user_id)
		return res
	return make_response(jsonify({'status':404, 'message':'user not found'}),404)

@user_blueprint.route('/users/<int:user_id>',methods =['PATCH'])
@tokenizer
def update_user(user_id):
	"""Given that i am an admin i should update specific user details """
	errors = []
	if user_id:
		user = User()
		if not request.get_json():
			return make_response(jsonify({'status':400,'message': 'Post data missing'}),400)
		post_data = request.get_json()
		name =  post_data['name']
		phone =  post_data['phone']
		email =  post_data['email']
		photo =  post_data['photo']
		password = post_data['password']
		national_id = post_data['national_id']
		check_missingfields= validate.missing_value_validator(['name','phone','email','photo','password','national_id'],post_data)
		if  check_missingfields !=True:errors.append(check_missingfields)
		check_emptyfield = validate.empty_string_validator(['name','phone','email','photo','password'],post_data)
		if check_emptyfield !=True:errors.append(check_emptyfield)
		check_if_integer = validate.is_integer_validator(['national_id'],post_data)
		if check_if_integer !=True:errors.append(check_if_integer)
		check_if_validurl = validate.is_valid_url(photo)
		if check_if_validurl !=True:errors.append(check_if_validurl)
		check_if_valid_email = validate.is_validEmail(email)
		if check_if_valid_email !=True:errors.append(check_if_valid_email)
		check_if_text_only = validate.is_text_only(name)
		if check_if_text_only !=True:errors.append(check_if_text_only)
		new_user = {}
		new_user['name'] =  name
		new_user['phone'] =  phone
		new_user['email'] =  email
		new_user['photo'] =  photo
		new_user['national_id'] =  national_id
		if len(errors) > 0:
			for e in errors:return e
		res = user.update_user(user_id,new_user)
		return res

@user_blueprint.route('/users/<int:user_id>',methods = ['DELETE'])
@tokenizer
def delete_user(user_id):
	"""Given that i am an admin i should be able to delete a specific user"""
	if user_id:
		check_if_integer = validate.is_single_integer(user_id)
		if check_if_integer !=True:return check_if_integer
		user = User()
		res = user.delete_user(user_id)
		return res

@user_blueprint.route('login',methods =['POST'])
def login():
	"""Given that i am a registered user i should be able to login"""
	if not request.get_json():
		return make_response(jsonify({"status":409,"message":"missing post data"}))
	post_data = request.get_json()
	users = User()
	res = users.login(post_data['email'],post_data['password'])
	return res



