from flask import request, jsonify, Blueprint, make_response
from app.api.v1.office.model import Office, offices

office_Blueprint = Blueprint('office', __name__)


@office_Blueprint.route('/offices')
def get_offices():
    """Given that i am an admin i should be able to get a list of all political offices
     When i visit .../api/v1/offices endpoint using GET method"""
    return make_response(jsonify(offices), 201)


@office_Blueprint.route('/offices', methods=['POST'])
def add_office():
    """Given that i am an admin i should be able to add a political office
       When i visit ../api/v1/offices endpoint using POST method"""
    try:
        if not request.get_json():
            return make_response(jsonify({'status': 401, "message": "missing input data"}), 401)
        office_data = request.get_json(force=True)
        office_name = office_data['office_name']
        logo = office_data['logo']
        office = Office()
        office.add_office(office_name, logo)
        return make_response(jsonify({
            "status": 201,
            "message": "Office added successfully",
            "offices": offices

        }), 201)

    except Exception as e:
        return make_response(jsonify({'message': e, 'status': 400}), 400)


@office_Blueprint.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """Given that i am an admin i should be able to get a specific l political office
       When i append party_id to .../api/v1/offices endpoint using GET method"""
    if office_id:
        if office_id in offices:
            return make_response(jsonify({'status': 201, 'office_data': offices.get(office_id)}), 201)
        return make_response(jsonify({'status': 404, 'message': 'party not found'}), 404)
    return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))

@office_Blueprint.route('/offices/<int:office_id>', methods=['PATCH'])
def update_office(office_id):
    """Given that i am an admin i should be able to edit a specific political office
       When i visit to .../api/v1/offices endpoint using PATCH method"""

    if office_id:
        if not request.get_json():
            return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
        office_data = request.get_json()
        office_name = office_data['office_name']
        logo = office_data['logo']
        office = Office()
        res = office.edit_office(office_id, office_name, logo)
        return res
    else:
        return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))


@office_Blueprint.route('/offices/<int:office_id>', methods=['DELETE'])
def delete_office(office_id):
    """Given that i am an admin i should be able to delete a specific political office
       When i append party_id to .../api/v1/offices endpoint using DELETE method"""
       When i append party_id to .../api/v1/delete_office endpoint using DELETE method"""
    if office_id:
        if office_id not in offices:
            return make_response(jsonify({
                "status": 404,
                "Product": "Office not found"
            }), 404)
        del offices[office_id]
        return make_response(jsonify({
            "status": 201,
            "Message": "Office deleted  successfully",
            "offices": offices
        }), 201)
    return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))
