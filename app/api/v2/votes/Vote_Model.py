from flask import make_response, jsonify, request
import psycopg2
import psycopg2.extras
from connection import connect

conn = connect()
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
parties = {}


class Votes(object):

    def cast_vote(self, createdby, office, candidate):
        """This method saves votes data"""
        try:

            cur.execute("SELECT * FROM tbl_candidates where  id = %s" %candidate)
            row = cur.fetchall()
            size = len(row)
            if not size > 0:
                return make_response(jsonify({'status': 409, 'message': 'invalid candidate '}), 409)
            cur.execute("SELECT * FROM tbl_offices where  id = %s" %office)
            row = cur.fetchall()
            size = len(row)
            if not size > 0:
                return make_response(jsonify({'status': 404, 'message': 'invalid office'}), 404)
            cur.execute("SELECT * FROM tbl_users where  id = %s"% createdby)
            row = cur.fetchall()
            size = len(row)
            if not size > 0:
                return make_response(jsonify({'status': 404, 'message': 'invalid voter'}), 404)
            cur.execute("SELECT * FROM tbl_votes where  createdby = %s and office = %s ",(createdby,office,))
            row2 = cur.fetchall()
            size2 = len(row2)
            # if not size2 > 0:
                # return make_response(jsonify({'status': 409, 'message': 'You have voted for another candidate in this '
                #                                                         'office '}), 409)
            cur.execute("SELECT * FROM tbl_votes where  createdby = %s and candidate = %s",
                        (createdby, candidate,))
            row = cur.fetchall()
            size = len(row)
            if size > 0:
                return make_response(jsonify({'status': 409, 'message': 'you have already voted for this candidate'}),
                                     409)

            cur.execute("INSERT INTO tbl_votes(createdby,office,candidate) VALUES(%s ,%s ,%s)",
                        (createdby, office, candidate))
            return make_response(jsonify({'status': 201, 'message': 'voted  successfully'}), 201)
        except psycopg2.DatabaseError as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status": 409, "message": str(splited[1].replace("Key", " ")).strip()}), 409)

    def get_results(self, office_id):
        """This method returns results of vote cast in a specific office"""
        try:
            cur.execute("SELECT * FROM tbl_offices where  id = %s" % office_id)
            row = cur.fetchall()
            size = len(row)
            if not size > 0:
                return make_response(jsonify({'status': 404, 'message': 'invalid office'}), 404)
            cur.execute("SELECT * FROM tbl_candidates JOIN tbl_users ON tbl_candidates.candidate=tbl_users.id WHERE office= %s" % office_id)
            candidates = cur.fetchall()
            size = len(candidates)
            main_votes = []
            if size > 0:
                for candidate in candidates:
                    cur.execute("SELECT candidate , COUNT(*) as votes from tbl_votes where candidate = %s group by candidate" % candidate["candidate"])
                    votes = cur.fetchall()
                    main_votes.append({"candidate":candidate["firstname"], "votes": len(votes)+1})

                return make_response(jsonify({'status': 200, 'data': main_votes,"Votes for ": str(row[0]["name"])}), 200)
            return make_response(jsonify({'status': 404, 'message': 'No available candidates for '+str(row[0]["name"])+' office'}), 404)
        except psycopg2.DatabaseError as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status": 409, "message": str(splited[1].replace("Key", " ")).strip()}), 409)
