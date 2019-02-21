from flask import make_response, jsonify, request

parties = {}


class Party(object):
    def __init__(self):
        self.party_id = 0
        self.party_name = ''
        self.logo = ''
        self.members = ''
        self.parties = parties

    @staticmethod
    def add_party(party_name, logo, members):
        """This method saves party data"""
        size = len(parties) + 1
        new_party = {
            "party_id": size,
            "party_name": party_name,
            "logo": logo,
            "members": members
        }
        parties[size] = new_party

    def get_parties(self):
        """This method shows all political parties in the dictionary"""
        return self.parties

    def edit_party(self, party_id, party_name, logo, members):
        """This method edits  a specific political party in the dictionary"""
        if party_id:
            if party_id in self.parties:
                parties[party_id]['party_name'] = party_name
                parties[party_id]['logo'] = logo
                parties[party_id]['members'] = members

                return make_response(jsonify({
                    "status": 201,
                    "message": "Party Updated successfully",
                    "new details": self.parties
                }), 201)
        return make_response(jsonify({
            "status": 404,
            "Message": "party not found"
        }), 404)
