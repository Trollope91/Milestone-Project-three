from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os


class dbhelper():
    def __init__(self):
        connection = os.getenv('connection')
        self.Client = MongoClient(connection)
        dbname = os.getenv('dbname')
        self.db = self.Client[dbname]

    def authenticateUser(self, email, password):
        user = self.db.users.find_one({"email": email})

        if user['password_hash'] and check_password_hash(user['password_hash'], password):
            return user

        return None

    def register(self, email, password):
        # insert new user if it doesnt exist
        newuser = {
            'username': email,
            'password_hash': password,
            'email': email
        }
        userscollection = self.db['users']
        doesuserexist = userscollection.find_one({'email': email})
        if doesuserexist is None:
            result = userscollection.insert_one(newuser)
            return True

    def getuserbyusername(self, email):
        return self.db.users.find_one({"email": email})

    def updateuser(self, firstname, lastname, email, picture, bio, dob):
        # insert new user if it doesnt exist
        self.db.users.update_one({'email': email}, {'$set': {
                                 'firstname': firstname, 'lastname': lastname, 'profile_picture': picture, 'bio': bio, 'dob': dob}})