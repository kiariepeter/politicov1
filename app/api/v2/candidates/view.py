from flask import request, jsonify, Blueprint, make_response
from app.api.v2.candidates.C_Model import Candidate
from custom_validator import My_validator as validate
candidates = Candidate()
candidate_blueprint = Blueprint('candidates', __name__)


@candidate_blueprint.route('/candidates')
def get_all_candidates():
    """Given that i am an admin i should be able to get a list of all political candidates
     When i visit .../api/v2/candidates endpoint using GET method"""
    candidate = candidates.getall_candidates()
    if candidate:
        return candidate
    return make_response(jsonify({'status':404,'message':'no offices found'}),404)


@candidate_blueprint.route('/candidates', methods=['POST'])
def add_candidates():
    """Given that i am an admin i should be able to add a political office
       When i visit ../api/v2/candidates endpoint using POST method"""
    errors = []
    try:
        if not request.get_json():errors.append(make_response(jsonify({'status': 409, "message": "missing input data"}), 409))
        candidate_data = request.get_json()
        check_missingfields= validate.missing_value_validator(['party','office','candidate'],candidate_data)
        if  check_missingfields !=True:
            return check_missingfields
        is_integer_validator = validate.is_integer_validator(['party','office','candidate'],candidate_data)
        if is_integer_validator !=True:
            return is_integer_validator
        party = candidate_data['party']
        office = candidate_data['office']
        candidate = candidate_data['candidate']
        if len(errors) > 0:
            for e in errors:
                return e
        res = candidates.add_candidate(party, office, candidate )
        return res

    except Exception as e:
        return make_response(jsonify({'message': "something went wrong "+str(e.args[0]), 'status': 400}), 400)


@candidate_blueprint.route('/candidates/<int:candidate_id>', methods=['GET'])
def get_specific_candidate(candidate_id):
    """Given that i am an admin i should be able to get a specific candidates
       When i append candidate_id to .../api/v2/candidates endpoint using GET method"""
    if candidate_id:
        res = candidates.get_specific_candidate(candidate_id)
        return res
    return make_response(jsonify({'status': 401, 'message': 'candidate_id missing'}, 401))


@candidate_blueprint.route('/candidates/<int:candidate_id>', methods=['PATCH'])
def update_candidate(candidate_id):
    """Given that i am an admin i should be able to edit a specific candidates
       When i visit to .../api/v2/candidates endpoint using PATCH method"""

    if candidate_id:
        if not request.get_json():
            return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
        candidate_data = request.get_json()
        check_missingfields= validate.missing_value_validator(['party','office','candidate'],candidate_data)
        if  check_missingfields !=True:
            return check_missingfields
        is_integer_validator = validate.is_integer_validator(['party','office','candidate'],candidate_data)
        if is_integer_validator !=True:
            return is_integer_validator
        party = candidate_data['party']
        office = candidate_data['office']
        candidate = candidate_data['candidate']
        res = candidates.edit_candidate(candidate_id, [party,office,candidate])
        return res
    return make_response(jsonify({'status': 401, 'message': 'candidate_id missing'}, 401))


@candidate_blueprint.route('/candidates/<int:candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    """Given that i am an admin i should be able to delete a specific candidate
       When i append candidate_id to .../api/v2/candidates endpoint using DELETE method"""
    if candidate_id:
        res = candidates.delete_candidate(candidate_id)
        return res 
    return make_response(jsonify({'status': 409, 'message': 'candidate_id missing'}, 409))

