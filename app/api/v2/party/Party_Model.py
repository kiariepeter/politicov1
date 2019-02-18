from flask import make_response, jsonify, request
import psycopg2
import psycopg2.extras
from connection import connect
conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
parties = {}


class Party(object):


    def add_party(self,party_data):
        """This method saves party data"""
        try:
            cur.execute("INSERT INTO tbl_parties(name,hqAddress,logoUrl,slogan) VALUES(%s ,%s ,%s, %s)", (party_data[0],party_data[1],party_data[2],party_data[3]))
            return make_response(jsonify({'status':201,'message':'party added successfully'}),201)
        except psycopg2.DatabaseError as e:
            return make_response(jsonify({'status':409,'message':"failed to save data "+str(e.args[0]) }), 409)


    def all_parties(self):
        """querying the database to get all parties"""
        cur.execute("SELECT * FROM tbl_parties  order by id desc")
        rows = cur.fetchall()
        return make_response(jsonify({'status':201,'data':rows}),201)

    def get_party(self,party_id):
        """ This returns all offices """
        cur.execute("SELECT * FROM tbl_parties where  id = %s",(str(party_id)))
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            return make_response(jsonify({'status':201, 'data': row}), 201)
        return make_response(jsonify({'status':404, 'message': 'party not found'}),404)

    def edit_party(self, party_id, party_data):
        """This method edits  a specific political party in the table"""
        if party_id:
            cur.execute("SELECT * FROM tbl_parties where  id = %s",(str(party_id)))
            row = cur.fetchall()
            size =len(row)
            if  size > 0:
                cur.execute("UPDATE tbl_parties set name= %s, hqAddress= %s, logoUrl= %s,slogan= %s WHERE id = %s",(party_data[0],party_data[1],party_data[2],party_data[3],str(party_id)))
                return make_response(jsonify({
                    "status": 201,
                    "message": "Party Updated successfully"
                }), 201)
            return make_response(jsonify({'status': 404, 'message': 'party not found'}), 404)
        return make_response(jsonify({'status': 401, 'message': 'missing party id'}))

    def party_delete(self,party_id):
        """This method deletes specific party by id"""
        cur.execute("SELECT * FROM tbl_parties where  id = %s",(str(party_id)))
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            cur.execute("DELETE  FROM  tbl_parties  WHERE id = %s",(str(party_id)))
            return make_response(jsonify({'status':201, 'message': "Party deleted successfully"}), 201)
        return make_response(jsonify({'status':404, 'message': 'Party not found'}),404)
