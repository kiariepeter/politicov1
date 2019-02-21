from flask import make_response, jsonify, request

offices = {}


class Office(object):
    def __init__(self):
        self.office_id = 0
        self.office_name = ''
        self.logo = ''
        self.offices = offices

    @staticmethod
    def add_office(office_name, logo):
        """This method saves Office data and adds it to the offices dictionary"""
        office_id = len(offices) + 1
        new_office = {
            "office_id": office_id,
            "office_name": office_name,
            "logo": logo
        }
        offices[office_id] = new_office

    @property
    def get_offices(self):
        """ This returns all offices """
        return self.offices

    @staticmethod
    def edit_office(office_id, office_name, logo):
        """This method updates the office dictionary of a specific office"""
        if office_id:
            if office_id in offices:
                offices[office_id]['office_name'] = office_name
                offices[office_id]['logo'] = logo
                return make_response(jsonify({
                    "status": 201,
                    "message": "Office Updated successfully",
                    "new details": offices.get(office_id)
                }), 201)
            return make_response(jsonify({'status': 404, 'message': 'office not found'}), 404)
        return make_response(jsonify({'status': 401, 'message': 'missing office id'}))



