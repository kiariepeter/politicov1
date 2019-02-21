from flask import make_response, jsonify, session
import psycopg2
import psycopg2.extras
from connection import connect
import json
import jwt
import datetime
import os

MY_APIKEY = os.getenv('MY_APIKEY')
conn = connect()
# import pdb;pdb.set_trace()
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
users = {}


class User(object):
    """user class for User"""

    def create_user(self, users):
        """This method saves user data in the database"""
        try:
            cur.execute(
                "INSERT INTO tbl_users(firstname,lastname,othername,phoneNumber,"
                "passportUrl,email,password) VALUES(%s ,%s ,%s, %s, %s, %s, %s)",
                (users[0], users[1], users[2], users[3], users[4], users[5], users[6]))
            cur.execute("SELECT * FROM tbl_users  order by id desc limit 1")
            users = cur.fetchall()
            token = jwt.encode({'user':users[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},
                               MY_APIKEY)
            return make_response(jsonify({'status': 201,'message': 'user added successfully', 'data': users}), 201)
        except psycopg2.DatabaseError as e:
            err = str(e.args[0])
            splited = err.split(": ")
            return make_response(jsonify({"status":409,"message":str(splited[1].replace("Key"," ")).strip()}),409)

    def get_users(self):
        """querying the database to get all users"""
        cur.execute("SELECT * FROM tbl_users  order by id desc")
        rows = cur.fetchall()
        return make_response(jsonify({'status': 200, 'data': rows}), 200)

    def get_userByid(self, user_id: object) -> object:
        """This method returns a specific user by id"""
        cur.execute("SELECT * FROM tbl_users where id = %s", (user_id,))
        row = cur.fetchall()
        size = len(row)
        if size > 0:
            return make_response(jsonify({'status': 200, 'data': row}), 200)
        return make_response(jsonify({'status': 404, 'message': 'user not found'}), 404)

    @staticmethod
    def login(email, password):
        session["username"] = "admin"
        res = str(session.items())
        """This method validates user credentials"""
        cur.execute("SELECT * FROM tbl_users where  email = %s and password = %s", (email, password))
        row = cur.fetchall()
        size = len(row)
        if size > 0:
            token = jwt.encode({'user': row[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},
                               MY_APIKEY)
            return make_response(jsonify(
                {'status': 200, "message": "logged in successfully", "data": row, 'token': token.decode('UTF-8')}), 200)
        return make_response(jsonify({'status': 404, "message": "user not found "}),404)

    def update_user(self, user_id, user_data):
        """This method updates specific user details"""
        cur.execute("SELECT * FROM tbl_users where  id = %s", (user_id,))
        row = cur.fetchall()
        size = len(row)
        if size > 0:
            cur.execute(
                "UPDATE tbl_users set firstname = %s,lastname= %s,othername = %s,phoneNumber= %s, passportUrl= %s,email= %s  WHERE id = %s",
                (user_data['firstname'], user_data['lastname'], user_data['othername'], user_data['phoneNumber'],
                 user_data['passportUrl'], user_data['email'], str(user_id)))
            return make_response(jsonify({'status': 200, 'message': "user updated successfully","data":row}), 200)
        return make_response(jsonify({'status': 404, 'message': 'user not found'}), 404)

    def delete_user(self, user_id: object) -> object:
        """This method deletes specific user by id"""
        cur.execute("SELECT * FROM tbl_users where  id = %s", (user_id,))
        row = cur.fetchall()
        size = len(row)
        if size > 0:
            cur.execute("DELETE  FROM  tbl_users  WHERE id = %s", (user_id,))
            return make_response(jsonify({'status': 200, 'message': "user deleted successfully"}), 200)
        return make_response(jsonify({'status': 404, 'message': 'user not found'}), 404)
