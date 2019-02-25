import validators
import re
from flask import Flask, make_response,jsonify
class My_validator(object):

	@staticmethod
	def missing_value_validator(input_data: object, post_data: object) -> object:
		"""This method checks if the posted data has all expected fields """
		for x in input_data:
			if x not in post_data:
				return make_response(jsonify({"status":404, "message":"missing element "+x}),404)
		return True

	@staticmethod
	def empty_string_validator(input_data: object, post_data: object) -> object:
		"""This method checks if all posted fields have empty input"""
		for v in input_data:
			if len(post_data[v].strip()) == 0:
				return make_response(jsonify({"status":409, "message":"empty input "+v}), 409)
		return True
	@staticmethod
	def is_integer_validator(input_data,post_data):
		"""This method checks if posted value is an integer"""
		for x in input_data:
			if not isinstance(post_data[x],int):
				return make_response(jsonify({"status":409, "message": "This is not an integer "+x }), 409)
		return True
	@staticmethod
	def is_single_integer(value):
		"""checking if a single value is an integer"""
		if not isinstance(value, int):
			return make_response(jsonify({"status":409, "message": "This is not an integer "+value }), 409)
		return True

	@staticmethod
	def is_valid_url(url):
		"""This method checks if  the url submitted is valid"""
		if  not validators.url(url):
			return make_response(jsonify({"status": 409, "message":"invalid url "+url}), 409)
		return True
		
	@staticmethod
	def is_validEmail(email):
		"""This checks if the submitted email is valid"""
		if not isinstance(email, str):
			return make_response(jsonify({"status": 409, "message": "email can only be a string" + email}),
								 409)

		if not email[0].isalpha():
			return make_response(jsonify({"status": 409, "message": "Not a valid email start with a letter" + email}), 409)
		if not validators.email(email):
			return make_response(jsonify({"status":409, "message":"Not a valid email "+email}), 409)
		return True

	@staticmethod
	def is_text_only(word):
		"""This method checks is word submitted contains letters only"""
		if not isinstance(word,str):
			return make_response(jsonify({"status":400, "message": word+" should contain letters only"}))
		if not word.isalpha():
			return make_response(jsonify({"status":400,"message": word+" should contain letters only "}), 400)
		return True
	@staticmethod
	def text_arrayvalidator(input_data,post_data):
		"""checks text input fields contains text letters only"""
		for x in input_data:
			if not isinstance(post_data[x],str):
				return make_response(jsonify({"status": 409, "message": post_data[x] + " should contain letters only"}),
									 409)
			if not post_data[x].isalpha():
				return make_response(jsonify({"status":409, "message": post_data[x]+" should contain letters only"}),409)
		return True
	@staticmethod
	def is_numbers(number):
		"""This method validates numbers submitted should only contain numbers"""
		if  number.isdigit():
			return True
		return make_response(jsonify({"status":409, "message": number+ "This should contain numbers only"}), 409)

	@staticmethod
	def is_strong_password(password):
		if len(password) < 6:
			return make_response(jsonify({"status": 401, "message": "password should contain more than six characters"}), 401)
		if re.search(r"\d", password) is None:
			return make_response(
				jsonify({"status": 401, "message": "password should contain a number"}), 401)
		if re.search(r"[A-Z]", password) is None:
			return make_response(jsonify({"status": 401, "message": "password should contain an Upper case letter"}), 401)
		if re.search(r"[a-z]", password) is None:
			return make_response(jsonify({"status": 401, "message": "password should contain an Lower case letter"}), 401)
		if re.search(r"\W", password) is None:
			return make_response(jsonify({"status": 401, "message": "password should contain a special character"}), 401)
		return True



		



