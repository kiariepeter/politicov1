from flask import request, jsonify, Blueprint, make_response,session

import jwt
from functools import wraps
import datetime
import json
import os
MY_APIKEY = os.getenv('MY_APIKEY')

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
			return make_response(jsonify({'status':400, 'message':'expired token '}),400)
		return f(*args, **kwargs)
	return my_wrapper

def is_admin():
	token = request.headers['x-access-token']
	data = jwt.decode(token, MY_APIKEY)
	if data["user"]["admin"] is not True:
		return make_response(jsonify({'status': 403, 'message': 'forbidden access is denied'}), 403)
	return True




