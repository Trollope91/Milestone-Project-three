from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from models.user import User

class dbhelper():
    def __init__(self):
        connection = os.getenv('connection')
        self.Client = MongoClient(connection)
        dbname = os.getenv('dbname')
        self.db = self.Client[dbname]

    def authenticateUser(self, email, password):
        user = self.db.users.find_one({"email": email})
        if user:
            if user['password_hash'] and check_password_hash(user['password_hash'], password):
                return user

        return None

    def register(self, email, password):
        newuser = {
            'username': email,
            'password_hash': password,
            'email': email
        }
        userscollection = self.db['users']
        doesuserexist = userscollection.find_one({'email': email})

        lastDocument = userscollection.find_one(sort=[('id', -1)])

        if lastDocument:
            latest_id = lastDocument.get('id', 0)
            next_id = latest_id + 1
        else:
            next_id = 1

        new_user_data = {
            'id': next_id,
            'username': newuser['username'],
            'password_hash': newuser['password_hash'],
            'email': newuser['email']
        }

        if doesuserexist is None:
            anew_user = User(new_user_data)
            result = userscollection.insert_one(
                anew_user.__dict__)

            return True

    def getuserbyusername(self, email):
        return self.db.users.find_one({"email": email})

    def updateuser(self, firstname, lastname, email, picture, bio, dob):
        self.db.users.update_one({'email': email}, {'$set': {
                                 'firstname': firstname, 'lastname': lastname, 'profile_picture': picture, 'bio': bio, 'dob': dob}})

    def deleteuser(self, email):
        self.db.users.delete_one({'email': email})                             

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
    
    def get_favourite_users(self, user, search=None):
        user_matches = self.db.matches.find({"user_id_one": user['id']})

        favorite_user_ids = set()
        for match in user_matches:
            if match["user_id_two"] != user['id']:
                favorite_user_ids.add(match["user_id_two"])

        query = {"id": {"$in": list(favorite_user_ids)}}

        if search:
            search_criteria = [
                {"firstname": {"$regex": search, "$options": "i"}},
                {"lastname": {"$regex": search, "$options": "i"}},
                {"bio": {"$regex": search, "$options": "i"}},
            ]

            query["$and"] = [{"$or": search_criteria}]

        favorite_users = list(self.db.users.find(query))

        return favorite_users

    def removeuserfromfavourite(self, user, favouriteuser):
        result = self.db.matches.delete_many({
            "user_id_one": user['id'],
            "user_id_two": favouriteuser
        })

        if result.deleted_count > 0:
            return True
        else:
            return False

    def updatepasswordforuser(self, user, new_password):
        self.db.users.update_one({'email': user['email']}, {'$set': {
                                 'password_hash': new_password}})

