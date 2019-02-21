from flask import make_response, jsonify, request
import psycopg2
import psycopg2.extras
from connection import connect
conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
parties = {}


class Candidate(object):


    def add_candidate(self,party, office, candidate ):
        """This method saves candidates data"""
        try:        
            cur.execute("SELECT * FROM tbl_parties where  id = %s" % party)
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':404, 'message': 'invalid party'}),404)
            cur.execute("SELECT * FROM tbl_offices where  id = %s" %office)
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':404, 'message': 'invalid office'}),404)
            cur.execute("SELECT * FROM tbl_users where  id = %s" %candidate)
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':404, 'message': 'invalid candidate'}),404)
            cur.execute("SELECT * FROM tbl_candidates where  candidate = %s" %candidate)
            row = cur.fetchall()
            size =len(row)
            if size > 0:
                return make_response(jsonify({'status':409, 'message': 'candidate already registered'}),409)
            cur.execute("INSERT INTO tbl_candidates(party,office,candidate) VALUES(%s ,%s ,%s)", (party,office,candidate))
            return make_response(jsonify({'status':201,'message':'candidate added successfully'}),201)
        except psycopg2.DatabaseError as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status": 409, "message": str(splited[1].replace("Key", " ")).strip()}), 409)


    def getall_candidates(self):
        """querying the database to get all candidates"""
        cur.execute("SELECT * FROM tbl_candidates  order by id desc")
        rows = cur.fetchall()
        return make_response(jsonify({'status':200,'data':rows}),200)

    def get_specific_candidate(self,candidate_id):
        """ This returns specific candidate data """
        cur.execute("SELECT * FROM tbl_candidates where  id = %s" %candidate_id)
        row = cur.fetchall()
        size =len(row)
        if  size > 0:
            return make_response(jsonify({'status':200, 'data': row}), 200)
        return make_response(jsonify({'status':404, 'message': 'candidate not found'}),404)

    def edit_candidate(self, candidate_id, candidate_data):
        """This method edits  a specific candidate in the table"""
        try:
            cur.execute("SELECT * FROM tbl_candidates where  candidate = %s" %candidate_id)
            row = cur.fetchall()
            size =len(row)
            if  size > 0:
                cur.execute("UPDATE tbl_candidates set party= %s, office= %s WHERE id = %s",(str(candidate_data[0]),str(candidate_data[1]),str(candidate_id),))
                return make_response(jsonify({
                    "status": 200,
                    "data":row,
                    "message": "Candidate Updated successfully"
                }), 200)
            return make_response(jsonify({'status': 404, 'message': 'Candidate not found'}), 404)
        except psycopg2.DatabaseError as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status": 409, "message": str(splited[1].replace("Key", " ")).strip()}), 409)

    def delete_candidate(self,candidate_id):
        """This method deletes specific candidate by id"""
        cur.execute("SELECT * FROM tbl_candidates where  id = %s",(str(candidate_id)))
        row = cur.fetchall()
        size =len(row)
        if size > 0:
            cur.execute("DELETE  FROM  tbl_candidates  WHERE id = %s",(str(candidate_id)))
            return make_response(jsonify({'status':200, 'message': "Candidate deleted successfully"}), 200)
        return make_response(jsonify({'status':404, 'message': 'Candidate not found'}),404)
