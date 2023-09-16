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