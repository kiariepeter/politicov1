from flask import request,jsonify,Blueprint,make_response
from app.api.v1.party.model import Party,  parties
party_Blueprint = Blueprint('party',__name__)

@party_Blueprint.route('/get_parties')
def index():
	return make_response(jsonify(parties),200)
	
@party_Blueprint.route('/add_party',methods = ['POST'])
def add_aparty():
	"""Given that i am an admin i should be able to add a political party
       When i visit .../api/v1/add_party endpoint using POST method"""
	try:
		if not request.get_json():
			return make_response(jsonify({'status':401}),401)
		party_data = request.get_json(force=True)
		party_name = party_data['party_name']
		logo=party_data['logo']
		members = party_data['members']
		party = Party(party_name,logo,members)
		party.add_party()
		return make_response(jsonify({
        "status": 201,
        "message": "Party added successfully",
        "parties": parties

    }), 201)

	except Exception as e:
		return make_response(jsonify({'message':'Bad request','status':400}),400)

@party_Blueprint.route('/get_party/<int:party_id>',methods =['GET'])
def get_party(party_id):
	if party_id:
		for party_dict in parties:
			for key in party_dict:
				if party_dict[key] == party_id:
					return make_response(jsonify({'status':201,'party_data':party_dict}),201)
				else:
					return make_response(jsonify({'status':404,'message':'party not found'}),404)

	else:
		return make_response(jsonify({'status':401,'message':'party_id missing'},401))



@party_Blueprint.route('/update_party/<int:party_id>',methods = ['PATCH'])
def update_party(party_id):
	if request.method =="PATCH":
		if party_id:
			if not request.get_json():
				return make_response(jsonify({'status':401,'message':'empty body'},401))
			party_data = request.get_json()
			party_name = party_data['party_name']
			logo=party_data['logo']
			members = party_data['members']
			party = Party(party_name,logo,members)
			res = party.edit_party(party_id)
			return res
		else:
			return make_response(jsonify({'status':401,'message':'party_id missing'},401))



@party_Blueprint.route('/delete_party/<int:party_id>',methods = ['DELETE'])
def delete_party(party_id):
	if request.method == "DELETE":
		if party_id:
			data = [parties for party in parties if party["party_id"] == party_id]
			if not data:
				return make_response(jsonify({
					"status": "OK",
					"Product": "Political party not found"
					}), 404)

			parties.remove(parties[0])
			return make_response(jsonify({
			"status": "OK",
			"Message": "Party deleted deleted successfully"
			}), 200)
		else:
			return make_response(jsonify({'status':401,'message':'party_id missing'},401))
	else:
		return make_response(jsonify({'message':'Bad request','status':400}),400)
