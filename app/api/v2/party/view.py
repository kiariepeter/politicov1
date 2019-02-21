from flask import request, jsonify, Blueprint, make_response
from app.api.v2.party.Party_Model import Party, parties
from custom_validator import My_validator as validate
from config import tokenizer, is_admin

party = Party()
party_blueprint = Blueprint('party', __name__)


@party_blueprint.route('/parties')
@tokenizer
def get_parties():
    """Given that i am an admin i should be able to get a list of all political parties
       When i visit .../api/v2/parties endpoint using GET method"""
    if is_admin() is not True:
        return is_admin()
    parties = party.all_parties()
    if parties:
        return parties
    return make_response(jsonify({'status': 404, 'message': 'no parties found'}), 404)


@party_blueprint.route('/parties', methods=['POST'])
@tokenizer
def add_party():
    """Given that i am an admin i should be able to add a political party
       When i visit .../api/v2/parties endpoint using POST method """
    if is_admin() is not True:
        return is_admin()
    try:
        if not request.get_json():
            return make_response(jsonify({'status': 401}), 401)
        party_data = request.get_json()
        check_missingfields = validate.missing_value_validator(['name', 'hqAddress', 'logoUrl', 'slogan'], party_data)
        if check_missingfields is not True:
            return check_missingfields
        check_emptyfield = validate.empty_string_validator(['name', 'hqAddress', 'logoUrl', 'slogan'], party_data)
        if check_emptyfield is not True:
            return check_emptyfield
        check_if_text_only = validate.text_arrayvalidator(['name', 'hqAddress'], party_data)
        if check_if_text_only is not True:  return check_if_text_only
        check_if_validurl = validate.is_valid_url(party_data['logoUrl'])
        if check_if_validurl is not True: return check_if_validurl
        name = party_data['name']
        hqAddress = party_data['hqAddress']
        logoUrl = party_data['logoUrl']
        slogan = party_data['slogan']

        res = party.add_party([name, hqAddress, logoUrl, slogan])
        return res
    except Exception as e:
        return make_response(jsonify({'message': 'Bad request ' + str(e.args[0]), 'status': 400}), 400)


@party_blueprint.route('/parties/<int:party_id>', methods=['GET'])
@tokenizer
def get_a_specific_party(party_id):
    """Given that i am an admin i should be able to get a  specific political party
       When i visit .../api/v2/parties/1 endpoint using GET method"""
    if is_admin() is not True:
        return is_admin()
    if party_id:
        res = party.get_party(party_id)
        return res
    return make_response(jsonify({'status': 401, 'message': 'party_id missing'}, 401))


@party_blueprint.route('/parties/<int:party_id>', methods=['PATCH'])
@tokenizer
def update_party(party_id):
    """Given that i am an admin i should be able to edit a specific political party
       When i visit to .../api/v2/parties endpoint using PUT method"""
    if is_admin() is not True:
        return is_admin()
    if not request.get_json():
        return make_response(jsonify({'status': 401, 'message': 'empty body'}, 401))
    party_data = request.get_json()
    check_missingfields = validate.missing_value_validator(['name', 'hqAddress', 'logoUrl', 'slogan'], party_data)
    if check_missingfields is not True:
        return check_missingfields
    check_emptyfield = validate.empty_string_validator(['name', 'hqAddress', 'logoUrl', 'slogan'], party_data)
    if check_emptyfield is not True:
        return check_emptyfield
    check_if_text_only = validate.text_arrayvalidator(['name', 'hqAddress'], party_data)
    if check_if_text_only is not True: return check_if_text_only
    check_if_validurl = validate.is_valid_url(party_data['logoUrl'])
    if check_if_validurl is not True: return check_if_validurl
    name = party_data['name']
    hqAddress = party_data['hqAddress']
    logoUrl = party_data['logoUrl']
    slogan = party_data['slogan']

    res = party.edit_party(party_id, [name, hqAddress, logoUrl, slogan])
    return res


@party_blueprint.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    """Given that i am an admin i should be able to delete a specific political party
       When i append party_id to .../api/v2/parties endpoint using DELETE method"""
    if is_admin() is not True:
        return is_admin()
    if party_id:
        res = party.party_delete(party_id)
        return res
    return make_response(jsonify({'status': 409, 'message': 'party_id missing'}, 409))
