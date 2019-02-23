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
            cur.execute("INSERT INTO tbl_offices(name,type) VALUES(%s ,%s) RETURNING *",(office_name,office_type))

            office_data = cur.fetchall()
            return make_response(jsonify({
            "status": 201,
            "message": "Office added successfully",
            "data":office_data
            }), 201)

        except (Exception, psycopg2.DatabaseError ) as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status":409,"message":str(splited[1].replace("Key"," ")).strip()}),409)

        
    def get_all_offices(self):
        """querying the database to get all users"""
        cur.execute("SELECT * FROM tbl_offices  order by id desc")
        rows = cur.fetchall()
        return make_response(jsonify({'status':200,'data':rows}),200)


    def get_office(self,office_id):
        """ This returns all offices """
        id = (str(office_id))
        cur.execute("SELECT * FROM tbl_offices where  id = '%s'" % id)
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            return make_response(jsonify({'status':200, 'data': row}), 200)
        return make_response(jsonify({'status':404, 'message': 'office not found'}),404)

    @staticmethod
    def edit_office(office_id, office_name, office_type):
        """This method updates data  of a specific office"""
        try:
            id = (str(office_id))
            cur.execute("SELECT * FROM tbl_offices where  id = '%s'" % id)
            row = cur.fetchall()
            size =len(row)
            if  size > 0:
                cur.execute("UPDATE tbl_offices set name= %s,type= %s WHERE id = %s RETURNING * ", (office_name, office_type, id))
                return make_response(jsonify({
                    "status": 200,
                    "data":row,
                    "message": "Office Updated successfully"
                }), 200)
            return make_response(jsonify({'status': 404, 'message': 'office not found'}), 404)
        except (Exception, psycopg2.DatabaseError ) as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status":409,"message":str(splited[1].replace("Key"," ")).strip()}),409)

    def deleteoffice(self,office_id):
        """This method deletes specific office by id"""
        cur.execute("SELECT * FROM tbl_offices where  id = %s" % office_id)
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            cur.execute("DELETE  FROM  tbl_offices  WHERE id = %s" % office_id)
            return make_response(jsonify({'status':200, 'message': "office deleted successfully"}), 200)
        return make_response(jsonify({'status':404, 'message': 'office not found'}),404)



