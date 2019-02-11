from flask import request, jsonify, Blueprint, make_response
from app.api.v1.office.model import Office, offices

office_Blueprint = Blueprint('office', __name__)


@office_Blueprint.route('/get_offices')
def get_offices():
    """Given that i am an admin i should be able to get a list of all political offices
     When i visit .../api/v1/get_offices endpoint using GET method"""
    return make_response(jsonify(offices), 201)


@office_Blueprint.route('/add_office', methods=['POST'])
def add_office():
    """Given that i am an admin i should be able to add a political office
       When i visit ../api/v1/add_office endpoint using POST method"""
    try:
        if not request.get_json():
            return make_response(jsonify({'status': 401}), 401)
        office_data = request.get_json(force=True)
        office_name = office_data['office_name']
        logo = office_data['logo']
        office = Office(office_name, logo)
        office.add_office()
        return make_response(jsonify({
            "status": 201,
            "message": "Office added successfully",
            "offices": offices

        }), 201)

    except Exception as e:
        return make_response(jsonify({'message': e, 'status': 400}), 400)


@office_Blueprint.route('/get_office/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """Given that i am an admin i should be able to get a specific l political office
       When i append party_id to .../api/v1/get_office endpoint using GET method"""
    if office_id:
        for office_dict in offices:
            for key in office_dict:
                if office_dict[key] == office_id:
                    return make_response(jsonify({'status': 201, 'office_data': office_dict}), 201)
                else:
                    return make_response(jsonify({'status': 404, 'message': 'party not found'}), 404)

    else:
        return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))


@office_Blueprint.route('/update_office/<int:office_id>', methods=['PATCH'])
def update_office(office_id):
    """Given that i am an admin i should be able to edit a specific political office
       When i visit to .../api/v1/edit_office endpoint using PATCH method"""
    if request.method == "PATCH":
        if office_id:
            if not request.get_json():
                return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
            office_data = request.get_json()
            office_name = office_data['office_name']
            logo = office_data['logo']
            office = Office(office_name, logo)
            res = office.edit_office(office_id)
            return res
        else:
            return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))


@office_Blueprint.route('/delete_office/<int:office_id>', methods=['DELETE'])
def delete_office(office_id):
    """Given that i am an admin i should be able to delete a specific political office
       When i append party_id to .../api/v1/delete_office endpoint using DELETE method"""
    if request.method == "DELETE":
        if office_id:
            data = [office for office in offices if office["office_id"] == office_id]
            if not data:
                return make_response(jsonify({
                    "status": 404,
                    "Product": "Office not found"
                }), 404)

            offices.remove(offices[0])
            return make_response(jsonify({
                "status": 201,
                "Message": "Office deleted deleted successfully"
            }), 201)
        else:
            return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))
    else:
        return make_response(jsonify({'message': 'Bad request', 'status': 400}), 400)
