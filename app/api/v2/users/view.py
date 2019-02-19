from flask import request, jsonify, Blueprint, make_response
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app.api.v2.users.Usermodel import User, users
from config import tokenizer
from custom_validator import My_validator as validate


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/auth/signup',methods = ['POST'])
def add_user():
	"""Given that am a new user i should be able to register"""
	errors = []

	try:
		if not request.get_json():error.append(make_response(jsonify({'status':404 , 'message':'missing input'}),404))
		post_data = request.get_json()
		check_missingfields= validate.missing_value_validator(['firstname','lastname','othername','email','phoneNumber','passportUrl','password'],post_data)
		if  check_missingfields !=True:return check_missingfields
		check_emptyfield = validate.empty_string_validator(['firstname','lastname','othername','email','phoneNumber','passportUrl','password'],post_data)
		if check_emptyfield !=True:errors.append(check_emptyfield)
		firstname =  post_data['firstname']
		lastname =  post_data['lastname']
		othername =  post_data['othername']
		phoneNumber =  post_data['phoneNumber']
		passportUrl = post_data['passportUrl']
		email = post_data['email']
		password = post_data['password']
		check_if_validurl = validate.is_valid_url(passportUrl)
		if check_if_validurl !=True:errors.append(check_if_validurl)
		check_if_valid_email = validate.is_validEmail(email)
		if check_if_valid_email !=True:errors.append(check_if_valid_email)
		check_if_text_only = validate.text_arrayvalidator(['firstname','lastname','othername'],post_data)
		if check_if_text_only !=True:errors.append(check_if_text_only)
		if len(errors) > 0:
			for e in errors:
				return e
		user = User()
		res = user.create_user([firstname,lastname,othername,phoneNumber,passportUrl,email,password])
		return res
	except KeyError as e:
		return make_response(jsonify({'status':400 ,'message':'bad request'}), 400)

@user_blueprint.route('/users',methods = ['GET'])
# @tokenizer
def get_all_users():
	"""Given that i am an admin i should view all registered users"""
	user = User()
	all_users = user.get_users()
	if all_users:
		return make_response(all_users,201)
	return make_response(jsonify({'status':404,'message':'no users found'}),404)

@user_blueprint.route('/users/<int:user_id>',methods = ['GET'])
# @tokenizer
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
# @tokenizer
def update_user(user_id):
	"""Given that i am an admin i should update specific user details """
	errors = []
	if user_id:
		user = User()
		if not request.get_json():
			return make_response(jsonify({'status':400,'message': 'Post data missing'}),400)
		post_data = request.get_json()
		post_data = request.get_json()
		check_missingfields= validate.missing_value_validator(['firstname','lastname','othername','email','phoneNumber','passportUrl','password'],post_data)
		if  check_missingfields !=True:return check_missingfields
		check_emptyfield = validate.empty_string_validator(['firstname','lastname','othername','email','phoneNumber','passportUrl','password'],post_data)
		if check_emptyfield !=True:errors.append(check_emptyfield)
		firstname =  post_data['firstname']
		lastname =  post_data['lastname']
		othername =  post_data['othername']
		phoneNumber =  post_data['phoneNumber']
		passportUrl = post_data['passportUrl']
		email = post_data['email']
		password = post_data['password']
		check_if_validurl = validate.is_valid_url(passportUrl)
		if check_if_validurl !=True:errors.append(check_if_validurl)
		check_if_valid_email = validate.is_validEmail(email)
		if check_if_valid_email !=True:errors.append(check_if_valid_email)
		check_if_text_only = validate.text_arrayvalidator(['firstname','lastname','othername'],post_data)
		if check_if_text_only !=True:errors.append(check_if_text_only)

		new_user = {}
		new_user['firstname'] =  firstname
		new_user['lastname'] =  lastname
		new_user['othername'] =  othername
		new_user['phoneNumber'] =  phoneNumber
		new_user['passportUrl'] =  passportUrl
		new_user['email'] =  email
		new_user['password'] =  password
		if len(errors) > 0:
			for e in errors:return e
		res = user.update_user(user_id,new_user)
		return res

@user_blueprint.route('/users/<int:user_id>',methods = ['DELETE'])
# @tokenizer
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



