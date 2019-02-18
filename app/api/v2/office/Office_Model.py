from flask import make_response, jsonify, request
import psycopg2
import psycopg2.extras
from connection import connect
conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
offices = {}


class Office(object):


    @staticmethod
    def add_office(office_name, office_type):
        """This method saves Office data and adds it to the offices table"""
        try:
            cur.execute("INSERT INTO tbl_offices(name,type) VALUES(%s ,%s)",(office_name,office_type))
            return make_response(jsonify({
            "status": 201,
            "message": "Office added successfully"
            }), 201)

        except (Exception, psycopg2.DatabaseError ) as e:
            return make_response(jsonify({"status":400,"message":"something went wrong "+str(e.args[0])}))

        
    def get_all_offices(self):
        """querying the database to get all users"""
        cur.execute("SELECT * FROM tbl_offices  order by id desc")
        rows = cur.fetchall()
        return make_response(jsonify({'status':201,'data':rows}),201)


    def get_office(self,office_id):
        """ This returns all offices """
        cur.execute("SELECT * FROM tbl_offices where  id = %s",(str(office_id)))
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            return make_response(jsonify({'status':201, 'data': row}), 201)
        return make_response(jsonify({'status':404, 'message': 'office not found'}),404)

    @staticmethod
    def edit_office(office_id, office_name, office_type):
        """This method updates data  of a specific office"""
        if office_id:
            cur.execute("SELECT * FROM tbl_offices where  id = %s",(str(office_id)))
            row = cur.fetchall()
            size =len(row)
            if  size > 0:
                cur.execute("UPDATE tbl_offices set name= %s,type= %s WHERE id = %s",(office_name,office_type,str(office_id)))
                return make_response(jsonify({
                    "status": 201,
                    "message": "Office Updated successfully"
                }), 201)
            return make_response(jsonify({'status': 404, 'message': 'office not found'}), 404)
        return make_response(jsonify({'status': 401, 'message': 'missing office id'}))
    def deleteoffice(self,office_id):
        """This method deletes specific office by id"""
        cur.execute("SELECT * FROM tbl_offices where  id = %s",(str(office_id)))
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            cur.execute("DELETE  FROM  tbl_offices  WHERE id = %s",(str(office_id)))
            return make_response(jsonify({'status':201, 'message': "office deleted successfully"}), 201)
        return make_response(jsonify({'status':404, 'message': 'office not found'}),404)



