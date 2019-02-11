from flask import make_response, jsonify, request

offices = []


class Office(object):
    def __init__(self, office_name, logo):
        self.office_id = len(offices) + 1
        self.office_name = office_name
        self.logo = logo
        self.offices = offices.append(
            {'office_id': 1, 'office_name': 'Office of the president', 'logo': 'http://www.lpolitio.com/logo.jpg'})

    def add_office(self):
        """This method saves Office data and appends it to the offices list"""
        new_office = {
            "office_id": len(offices) + 1,
            "office_name": self.office_name,
            "logo": self.logo
        }
        offices.append(new_office)

    def get_offices(self):
        return self.offices

    @staticmethod
    def edit_office(office_id):
        task = [office for office in offices if office["office_id"] == office_id]
        if not task:
            return make_response(jsonify({
                "status": "OK",
                "Message": "Office not found"
            }), 404)
        task[0]['logo'] = request.json.get('logo', task[0]['logo'])
        task[0]['office_name'] = request.json.get('office_name', task[0]['office_name'])
        return make_response(jsonify({
            "status": 201,
            "message": "Office Updated successfully",
            "new details": task[0]
        }), 201)



