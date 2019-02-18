from flask import request, jsonify, Blueprint, make_response
import jwt
from functools import wraps
import datetime
import json

MY_APIKEY = 'hj5499GFWDRWw988ek<MKL(IEI$NMR'
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
