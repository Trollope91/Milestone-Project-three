from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from models.user import User
from base64helper import compressimagefromfilepath


class dbhelper():
    def __init__(self):
        """
        Initializes the database helper.

        """
        connection = os.getenv('connection')
        self.Client = MongoClient(connection)
        dbname = os.getenv('dbname')
        self.db = self.Client[dbname]

    def authenticateUser(self, email, password):
        """
        Authenticates a user.

        """
        user = self.db.users.find_one({"email": email})
        if user:
            stored_password_hash = user.get('password_hash', '')
            if check_password_hash(stored_password_hash, password):
                return user

        return None

    def register(self, email, password):
        """
        Registers a new user.

        """
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
        """
        Gets user information by username.

        """
        return self.db.users.find_one({"email": email})

    def updateuser(self, firstname, lastname, email, picture, bio, dob):
        """
        Updates user information.

        """
        self.db.users.update_one({'email': email}, {'$set': {
            'firstname': firstname, 'lastname': lastname,
            'profile_picture': picture, 'bio': bio,
            'dob': dob}})

    def deleteuser(self, email):
        """
        Delete a user.

        """
        self.db.users.delete_one({'email': email})

    def getAllUsers(self):
        """
        Gets a list of all users.

        """
        userlist = list(self.db.users.find().sort("_id", -1).limit(16))
        return userlist

    def addusertofavourite(self, user, favouriteuser):
        """
        Adds a user to favorites.

        """
        match = {
            "user_id_one": user['id'],
            "user_id_two": favouriteuser,
            "progress": 100
        }
        self.db.matches.insert_one(match)
        return True

    def get_favourite_users(self, user, search=None):
        """
        Gets a list of favorite users.

        """
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
        """
        Remove a user from favorites.

        """
        result = self.db.matches.delete_many({
            "user_id_one": user['id'],
            "user_id_two": favouriteuser
        })

        if result.deleted_count > 0:
            return True
        else:
            return False

    def updatepasswordforuser(self, user, new_password):
        """
        Update a user's password.

        """
        self.db.users.update_one({'email': user['email']}, {'$set': {
            'password_hash': new_password}})

    def setup(self):
        userscollection = self.db['users']
        users = [
            {
                'id': 1,
                'bio': (
                    'Tech enthusiast and software developer. '
                    'Building innovative solutions for complex problems.'
                ),
                'firstname': 'John',
                'lastname': 'Smith',
                'username': 'john.smith',
                'password_hash': 'wz3AvmLS1B',
                'dob': '15-11-1985',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '30-04-2019',
                'phone_number': '+1-555-456-7890',
                'email': 'john.smith@example.com',
                'profile_picture': ''
            },
            {
                'id': 2,
                'bio': (
                    'Music lover and guitarist. '
                    'Playing melodies that soothe the soul.'
                ),
                'firstname': 'Michael',
                'lastname': 'Johnson',
                'username': 'michael.johnson',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '03-09-1979',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '09-11-2020',
                'phone_number': '+1-555-567-8901',
                'email': 'michael.johnson@example.com',
                'profile_picture': ''
            },
            {
                'id': 3,
                'bio': (
                    'Outdoor adventurer and nature enthusiast. '
                    'Exploring the beauty of the wilderness.'
                ),
                'firstname': 'William',
                'lastname': 'Brown',
                'username': 'william.brown',
                'password_hash': 'wzZjZdL4B1',
                'dob': '14-05-1983',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '10-07-2019',
                'phone_number': '+1-555-234-5678',
                'email': 'william.brown@example.com',
                'profile_picture': ''
            },
            {
                'id': 4,
                'bio': (
                    'Foodie and culinary artist. '
                    'Creating gastronomic delights for the taste buds.'
                ),
                'firstname': 'Daniel',
                'lastname': 'Davis',
                'username': 'daniel.davis',
                'password_hash': 'wzZj4cLB1B',
                'dob': '30-01-1992',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '25-03-2020',
                'phone_number': '+1-555-678-9012',
                'email': 'daniel.davis@example.com',
                'profile_picture': ''
            },
            {
                'id': 5,
                'bio': (
                    'Gamer and esports enthusiast. '
                    'Dominating virtual worlds one game at a time.'
                ),
                'firstname': 'James',
                'lastname': 'Garcia',
                'username': 'james.garcia',
                'password_hash': 'wzZj4cLB1B',
                'dob': '12-06-1987',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '17-10-2018',
                'phone_number': '+1-555-789-0123',
                'email': 'james.garcia@example.com',
                'profile_picture': ''
            },
            {
                'id': 6,
                'bio': (
                    'Fitness enthusiast and personal trainer. '
                    'Helping clients achieve their fitness goals.'
                ),
                'firstname': 'David',
                'lastname': 'Martinez',
                'username': 'david.martinez',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '08-03-1990',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '15-05-2019',
                'phone_number': '+1-555-345-6789',
                'email': 'david.martinez@example.com',
                'profile_picture': ''
            },
            {
                'id': 7,
                'bio': (
                    'Bookworm and literature lover. '
                    'Immersed in the world of books and stories.'
                ),
                'firstname': 'Joseph',
                'lastname': 'Wilson',
                'username': 'joseph.wilson',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '20-11-1993',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '08-12-2020',
                'phone_number': '+1-555-123-4567',
                'email': 'joseph.wilson@example.com',
                'profile_picture': ''
            },
            {
                'id': 8,
                'bio': (
                    'Art lover and aspiring painter. '
                    'Creating colorful and imaginative artwork.'
                ),
                'firstname': 'Matthew',
                'lastname': 'Harris',
                'username': 'matthew.harris',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '09-07-1991',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '20-01-2021',
                'phone_number': '+1-555-234-5678',
                'email': 'matthew.harris@example.com',
                'profile_picture': ''
            },
            {
                'id': 9,
                'bio': (
                    'Animal lover and volunteer at the local shelter. '
                    'Advocating for furry friends.'
                ),
                'firstname': 'Daniel',
                'lastname': 'Anderson',
                'username': 'daniel.anderson2',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '18-02-1986',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '22-03-2019',
                'phone_number': '+1-555-345-6789',
                'email': 'daniel.anderson2@example.com',
                'profile_picture': ''
            },
            {
                'id': 10,
                'bio': (
                    'Tech geek and coding enthusiast. '
                    'Building the future one line of code at a time.'
                ),
                'firstname': 'Michael',
                'lastname': 'Miller',
                'username': 'michael.miller',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '25-09-1984',
                'gender': 'male',
                'is_confirmed': 1,
                'created_at': '04-06-2021',
                'phone_number': '+1-555-456-7890',
                'email': 'michael.miller@example.com',
                'profile_picture': ''
            },
            {
                'id': 11,
                'bio': (
                    'Tech enthusiast and software developer. '
                    'Building innovative solutions for complex problems.'
                ),
                'firstname': 'Emily',
                'lastname': 'Johnson',
                'username': 'emily.johnson',
                'password_hash': 'wz3AvmLS1B',
                'dob': '05-03-1988',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '30-04-2019',
                'phone_number': '+1-555-456-7890',
                'email': 'emily.johnson@example.com',
                'profile_picture': ''
            },
            {
                'id': 12,
                'bio': (
                    'Music lover and pianist. '
                    'Playing melodies that touch the heart.'
                ),
                'firstname': 'Sophia',
                'lastname': 'Garcia',
                'username': 'sophia.garcia',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '10-09-1990',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '14-11-2020',
                'phone_number': '+1-555-567-8901',
                'email': 'sophia.garcia@example.com',
                'profile_picture': ''
            },
            {
                'id': 13,
                'bio': (
                    'Nature lover and hiker. '
                    'Exploring the beauty of the great outdoors.'
                ),
                'firstname': 'Olivia',
                'lastname': 'Brown',
                'username': 'olivia.brown',
                'password_hash': 'wzZjZdL4B1',
                'dob': '20-06-1985',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '18-07-2019',
                'phone_number': '+1-555-234-5678',
                'email': 'olivia.brown@example.com',
                'profile_picture': ''
            },
            {
                'id': 14,
                'bio': (
                    'Foodie and culinary artist. '
                    'Crafting delicious dishes that satisfy the palate.'
                ),
                'firstname': 'Mia',
                'lastname': 'Davis',
                'username': 'mia.davis',
                'password_hash': 'wzZj4cLB1B',
                'dob': '15-01-1991',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '22-03-2020',
                'phone_number': '+1-555-678-9012',
                'email': 'mia.davis@example.com',
                'profile_picture': ''
            },
            {
                'id': 15,
                'bio': (
                    'Gamer and Twitch streamer. '
                    'Streaming epic gaming adventures to the world.'
                ),
                'firstname': 'Chloe',
                'lastname': 'Wilson',
                'username': 'chloe.wilson',
                'password_hash': 'wzZj4cLB1B',
                'dob': '18-04-1993',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '19-10-2018',
                'phone_number': '+1-555-789-0123',
                'email': 'chloe.wilson@example.com',
                'profile_picture': ''
            },
            {
                'id': 16,
                'bio': (
                    'Fitness enthusiast and yoga instructor. '
                    'Spreading health and wellness.'
                ),
                'firstname': 'Ava',
                'lastname': 'Martinez',
                'username': 'ava.martinez',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '12-03-1987',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '15-09-2019',
                'phone_number': '+1-555-345-6789',
                'email': 'ava.martinez@example.com',
                'profile_picture': ''
            },
            {
                'id': 17,
                'bio': (
                    'Bookworm and literature enthusiast. '
                    'Exploring new worlds through books.'
                ),
                'firstname': 'Lily',
                'lastname': 'Harris',
                'username': 'lily.harris',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '08-02-1994',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '20-11-2020',
                'phone_number': '+1-555-123-4567',
                'email': 'lily.harris@example.com',
                'profile_picture': ''
            },
            {
                'id': 18,
                'bio': (
                    'Art lover and painter. '
                    'Creating colorful and imaginative artwork.'
                ),
                'firstname': 'Sophia',
                'lastname': 'Thomas',
                'username': 'sophia.thomas',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '29-07-1992',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '25-12-2019',
                'phone_number': '+1-555-234-5678',
                'email': 'sophia.thomas@example.com',
                'profile_picture': ''
            },
            {
                'id': 19,
                'bio': (
                    'Animal lover and volunteer at the local shelter. '
                    'Advocating for furry friends.'
                ),
                'firstname': 'Olivia',
                'lastname': 'Miller',
                'username': 'olivia.miller',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '11-05-1993',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '18-08-2019',
                'phone_number': '+1-555-678-9012',
                'email': 'olivia.miller@example.com',
                'profile_picture': ''
            },
            {
                'id': 20,
                'bio': (
                    'Tech geek and coding enthusiast. '
                    'Building the future one line of code at a time.'
                ),
                'firstname': 'Mia',
                'lastname': 'Taylor',
                'username': 'mia.taylor',
                'password_hash': 'wzZjZ4cLB1B',
                'dob': '05-12-1990',
                'gender': 'female',
                'is_confirmed': 1,
                'created_at': '22-06-2020',
                'phone_number': '+1-555-890-1234',
                'email': 'mia.taylor@example.com',
                'profile_picture': ''
            }
        ]

        picture_dir = os.getcwd() + '/static/profilepics/'
        profile_pictures = []
        for filename in os.listdir(picture_dir):
            if filename.startswith('profilepic') and filename.endswith('.jpg'):
                file_path = os.path.join(picture_dir, filename)
                base64_image = compressimagefromfilepath(file_path)
                if base64_image:
                    profile_pictures.append(base64_image)

        for i, user in enumerate(users):
            if i < len(profile_pictures):
                user['profile_picture'] = profile_pictures[i]
            else:
                user['profile_picture'] = ''

        for user in users:
            username = user['username']
            doesuserexist = userscollection.find_one({'username': username})
            if doesuserexist is None:
                result = userscollection.insert_one(user)
                print(result.inserted_id)
        # result = userscollection.insert_many(users)

        matchescollection = self.db['matches']
        matches = [{
            'id': 1,
            'user_id_one': 1,
            'user_id_two': 2,
            'progress': 25
        }]
        result = matchescollection.insert_many(matches)

        messagescollection = self.db['messages']
        messages = [{
            'id': 1,
            'sender_id_one': 1,
            'reciever_id_two': 2,
            'message': 'Hello!',
            'created_at': '29-08-2023 23:01',
            'is_read': 1,
            'is_delivered': 1
        }]
        result = messagescollection.insert_many(messages)

        user_settingscollection = self.db['user_settings']
        user_settings = [{
            'id': 1,
            'user_id': 1,
            'min_age': 25,
            'max_age': 35,
            'preferred_gender': 'Female',
            'location_radius': 50
        }]
        result = user_settingscollection.insert_many(user_settings)

        user_hobbiescollection = self.db['user_hobbies']
        user_hobbies = [{
            'id': 1,
            'user_id': 1,
            'hobby_id': 1
        }]
        result = user_hobbiescollection.insert_many(user_hobbies)

        hobbiescollection = self.db['hobbies']
        hobbies = [{
            'id': 1,
            'tag_name': 'reading'
        }]

        result = hobbiescollection.insert_many(hobbies)
