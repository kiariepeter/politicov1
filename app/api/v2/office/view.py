from flask import request, jsonify, Blueprint, make_response
from app.api.v2.office.Office_Model import Office, offices
from custom_validator import My_validator as validate
office = Office()
office_blueprint = Blueprint('office', __name__)


@office_blueprint.route('/offices')
def get_offices():
    """Given that i am an admin i should be able to get a list of all political offices
     When i visit .../api/v2/offices endpoint using GET method"""
    offices = office.get_all_offices()
    if offices:
        return offices
    return make_response(jsonify({'status':404,'message':'no offices found'}),404)


@office_blueprint.route('/offices', methods=['POST'])
def add_office():
    """Given that i am an admin i should be able to add a political office
       When i visit ../api/v2/offices endpoint using POST method"""
    errors = []
    try:
        if not request.get_json():errors.append(make_response(jsonify({'status': 409, "message": "missing input data"}), 409))
        office_data = request.get_json()
        check_missingfields= validate.missing_value_validator(['name','type'],office_data)
        if  check_missingfields !=True:
            return check_missingfields
        check_emptyfield = validate.empty_string_validator(['name','type'],office_data)
        if check_emptyfield !=True:
            return check_emptyfield
        check_if_text_only = validate.text_arrayvalidator(['name','type'],office_data)
        if check_if_text_only !=True:
            return check_if_text_only
        office_name = office_data['name']
        office_type = office_data['type']
        if len(errors) > 0:
            for e in errors:
                return e
        res = office.add_office(office_name, office_type)
        return res

    except Exception as e:
        return make_response(jsonify({'message': "something went wrong "+str(e.args[0]), 'status': 400}), 400)


@office_blueprint.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """Given that i am an admin i should be able to get a specific l political office
       When i append party_id to .../api/v2/offices endpoint using GET method"""
    if office_id:
        res = office.get_office(office_id)
        return res
    return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))


@office_blueprint.route('/offices/<int:office_id>', methods=['PATCH'])
def update_office(office_id):
    """Given that i am an admin i should be able to edit a specific political office
       When i visit to .../api/v2/offices endpoint using PATCH method"""

    if office_id:
        if not request.get_json():
            return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
        office_data = request.get_json()
        check_missingfields= validate.missing_value_validator(['name','type'],office_data)
        if  check_missingfields !=True:
            return check_missingfields
        check_emptyfield = validate.empty_string_validator(['name','type'],office_data)
        if check_emptyfield !=True:
            return check_emptyfield
        check_if_text_only = validate.text_arrayvalidator(['name','type'],office_data)
        if check_if_text_only !=True:
            return check_if_text_only
        office_name = office_data['name']
        office_type = office_data['type']
        res = office.edit_office(office_id, office_name, office_type)
        return res
    return make_response(jsonify({'status': 401, 'message': 'office_id missing'}, 401))


@office_blueprint.route('/offices/<int:office_id>', methods=['DELETE'])
def delete_office(office_id):
    """Given that i am an admin i should be able to delete a specific political office
       When i append party_id to .../api/v2/offices endpoint using DELETE method"""
    if office_id:
        res = office.deleteoffice(office_id)
        return res 
    return make_response(jsonify({'status': 409, 'message': 'office_id missing'}, 409))

