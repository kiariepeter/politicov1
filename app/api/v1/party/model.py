from flask import make_response, jsonify, request
parties = []
class Party(object):
	def __init__(self,party_name,logo,members):
		self.party_id = len(parties) + 1
		self.party_name = party_name
		self.logo = logo
		self.members = members
		self.parties = parties.append({'party_id':1,'party_name':'Nark','logo':'http://www.lpolitio.com/logo.jpg','members':40})
		
	def add_party(self):
		"""This method saves party data"""
		new_party = {
			"party_id": len(parties) + 1,
			"party_name": self.party_name,
			"logo": self.logo,
			"members": self.members
			}
		parties.append(new_party)

	def get_parties(self):
		"""This method shows all political parties in the list"""
		return self.parties
	@staticmethod
	def edit_party(party_id):
		task = [party for party in parties if party["party_id"] == party_id]
		if not task:
			return make_response(jsonify({
				"status": "OK",
                "Message": "party not found"
                }), 404)
		task[0]['members'] = request.json.get('members', task[0]['members'])
		task[0]['logo'] = request.json.get('logo', task[0]['logo'])
		task[0]['party_name'] = request.json.get('party_name', task[0]['party_name'])
		return make_response(jsonify({
			"status": 201,
			"message": "Party Updated successfully",
			"new details": task[0]
			}), 201)

        
	    	
