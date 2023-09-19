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
        
        lastDocument = userscollection.find_one(sort=[('id', -1)])
        
        if lastDocument:
            latest_id = lastDocument['id']
            next_id = latest_id + 1
        else:
            next_id = 1
            
        newuser["id"] = next_id
        if doesuserexist is None:
            result = userscollection.insert_one(newuser)
            return True

    def getuserbyusername(self, email):
        return self.db.users.find_one({"email": email})

    def updateuser(self, firstname, lastname, email, picture, bio, dob):
        # insert new user if it doesnt exist
        self.db.users.update_one({'email': email}, {'$set': {
                                 'firstname': firstname, 'lastname': lastname, 'profile_picture': picture, 'bio': bio, 'dob': dob}})

    def getAllUsers(self):
        userlist = list(self.db.users.find().sort("_id", -1).limit(16))
        return userlist

    def addusertofavourite(self, user, favouriteuser):
        
    
        match = {
            "user_id_one": user['id'],
            "user_id_two": favouriteuser,
            "progress": 100
        }    
        self.db.matches.insert_one(match)
        return True 
    
    def get_favourite_users(self, user):

        # Find matches for the user
        user_matches = self.db.matches.find({"user_id_one": user['id']})

        # Get all users id which are favourited by the user
        favorite_user_ids = set()
        for match in user_matches:
            if match["user_id_two"] != user['id']:
                favorite_user_ids.add(match["user_id_two"])

        # Retrieve the details of these favorite users
        favorite_users = list(self.db.users.find(
            {"id": {"$in": list(favorite_user_ids)}}))

        return favorite_users

