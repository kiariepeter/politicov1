from flask import make_response, jsonify, request
import psycopg2
import psycopg2.extras
from connection import connect
conn = connect()
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
parties = {}

class Votes(object):


    def cast_vote(self,createdby, office, candidate ):
        """This method saves votes data"""
        try:        

            cur.execute("SELECT * FROM tbl_candidates where  id = %s",(str(candidate)))
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':409, 'message': 'invalid candidate '}),409)

            cur.execute("SELECT * FROM tbl_offices where  id = %s",(str(office)))
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':404, 'message': 'invalid office'}),404)

            cur.execute("SELECT * FROM tbl_users where  id = %s",(str(createdby)))
            row = cur.fetchall()
            size =len(row)
            if not size > 0:
                return make_response(jsonify({'status':404, 'message': 'invalid voter'}),404)

            cur.execute("SELECT * FROM tbl_votes where  createdby = %s and candidate = %s",(str(createdby),str(candidate)))
            row = cur.fetchall()
            size =len(row)
            if size > 0:
                return make_response(jsonify({'status':409, 'message': 'you have already voted for this candidate'}),409)

            cur.execute("INSERT INTO tbl_votes(createdby,office,candidate) VALUES(%s ,%s ,%s)", (createdby,office,candidate))
            return make_response(jsonify({'status':201,'message':'voted  successfully'}),201)
        except psycopg2.DatabaseError as e:
            return make_response(jsonify({'status':409,'message':"failed to vote "+str(e.args[0]) }), 409)

    def get_results(self,office_id):
    	"""This method returns results of vote cast in a specific office"""
    	cur.execute("SELECT office, candidate,  COUNT(*) as result FROM tbl_votes WHERE office = %s GROUP BY candidate, office",(str(office_id)))
    	votes = cur.fetchall()
    	size =len(votes)
    	if size > 0:
    		return make_response(jsonify({'status':200, 'data': votes}),200)
    	return make_response(jsonify({'status':409, 'message': 'invalid candidate '}),409)