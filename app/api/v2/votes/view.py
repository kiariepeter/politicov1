from flask import request, jsonify, Blueprint, make_response
from app.api.v2.votes.Vote_Model import Votes
from custom_validator import My_validator as validate
votes = Votes()
votes_blueprint = Blueprint('votes', __name__)



@votes_blueprint.route('/vote', methods=['POST'])
def castvote():
    """Given that i am a registerd voter i should be able to cast my vote
       When i visit ../api/v2/vote endpoint using POST method"""
    errors = []
    try:
        if not request.get_json():errors.append(make_response(jsonify({'status': 409, "message": "missing input data"}), 409))
        vote_data = request.get_json()
        check_missingfields= validate.missing_value_validator(['createdby','office','candidate'],vote_data)
        if  check_missingfields !=True:
            return check_missingfields
        is_integer_validator = validate.is_integer_validator(['createdby','office','candidate'],vote_data)
        if is_integer_validator !=True:
            return is_integer_validator
        createdby = vote_data['createdby']
        office = vote_data['office']
        candidate = vote_data['candidate']
        if len(errors) > 0:
            for e in errors:
                return e
        res = votes.cast_vote(createdby, office, candidate )
        return res

    except Exception as e:
        return make_response(jsonify({'message': "something went wrong "+str(e.args[0]), 'status': 400}), 400)

@votes_blueprint.route('/vote/results/<int:office_id>', methods=['GET'])
def get_votes_results(office_id):
	"""This method returns results of all votes for a candidate in a specific office"""
	if office_id:
		results = votes.get_results(office_id)
		if results:
			return results
	return make_response(jsonify({"status":404, "message":"office_id missing"}))