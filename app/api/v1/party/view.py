from flask import request, jsonify, Blueprint, make_response
from app.api.v1.party.model import Party, parties

party_Blueprint = Blueprint('party', __name__)


@party_Blueprint.route('/parties')
def get_parties():
    """Given that i am an admin i should be able to get a list of all political parties
       When i visit .../api/v1/parties endpoint using GET method"""
    return make_response(jsonify(parties), 201)


@party_Blueprint.route('/parties', methods=['POST'])
def add_party():
    """Given that i am an admin i should be able to add a political party
       When i visit .../api/v1/parties endpoint using POST method """
    try:
        if not request.get_json():
            return make_response(jsonify({'status': 401}), 401)
        party_data = request.get_json(force=True)
        party_name = party_data['party_name']
        logo = party_data['logo']
        members = party_data['members']
        party = Party()
        party.add_party(party_name, logo, members)
        return make_response(jsonify({
            "status": 201,
            "message": "Party added successfully",
            "parties": parties

        }), 201)

    except Exception as e:
        return make_response(jsonify({'message': 'Bad request', 'status': 400}), 400)


@party_Blueprint.route('/parties/<int:party_id>', methods=['GET'])
def get_party(party_id):
    """Given that i am an admin i should be able to get a  specific political party
       When i visit .../api/v1/parties/1 endpoint using GET method"""
    if party_id:
        if party_id in parties:
            return make_response(jsonify({'status': 201, 'party': parties.get(party_id)}),201)
        return make_response(jsonify({'status': 404, 'message': 'party not found'}), 404)
    return make_response(jsonify({'status': 401, 'message': 'party_id missing'}, 401))


@party_Blueprint.route('/parties/<int:party_id>', methods=['PATCH'])
def update_party(party_id):
    """Given that i am an admin i should be able to edit a specific political party
       When i visit to .../api/v1/parties endpoint using PUT method"""
    if request.method == "PATCH":
        if party_id:
            if not request.get_json():
                return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
            party_data = request.get_json()
            party_name = party_data['party_name']
            logo = party_data['logo']
            members = party_data['members']
            party = Party()
            res = party.edit_party(party_id,party_name, logo, members)
            return res
        else:
            return make_response(jsonify({'status': 401, 'message': 'party_id missing'}, 401))


@party_Blueprint.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    """Given that i am an admin i should be able to delete a specific political party
       When i append party_id to .../api/v1/parties endpoint using DELETE method"""
    if request.method == "DELETE":
        if party_id:
            if party_id in parties:
                del parties[party_id]
                return make_response(jsonify({
                    "status": "OK",
                    "Message": "Party deleted deleted successfully",
                    'parties': parties
                }), 200)
            return make_response(jsonify({'status': 404, 'message': 'party not found'}), 404)

        return make_response(jsonify({'status': 401, 'message': 'party_id missing'}, 401))

    return make_response(jsonify({'message': 'Bad request', 'status': 400}), 400)
