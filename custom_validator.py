import validators
import json
from flask import Flask, make_response,jsonify
class My_validator(object):

	@staticmethod
	def missing_value_validator(input_data,post_data):
		"""This method checks if the posted data has all expected fields """
		for x in input_data:
			if x not in post_data:
				return make_response(jsonify({"status":404, "message":"missing element "+x}),404)
		return True

	@staticmethod
	def empty_string_validator(input_data,post_data):
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
		if not validators.url(url):
			return make_response(jsonify({"status": 409, "message":"invalid url "+url}), 409)
		return True
	@staticmethod
	def is_valid_email(email):
		"""This checks if the submitted email is valid"""
		if not validators.email(email):
			return make_response(jsonify({"status":409, "message":"Not a valid email "+email}), 409)
		return True


