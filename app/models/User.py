class User:
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.bio = user_data.get('bio', '')
        self.firstname = user_data.get('firstname', '')
        self.lastname = user_data.get('lastname', '')
        self.username = user_data.get('username', '')
        self.password_hash = user_data.get('password_hash', '')
        self.dob = user_data.get('dob', '')
        self.gender = user_data.get('gender', '')
        self.is_confirmed = user_data.get('is confirmed', 0)
        self.created_at = user_data.get('created_at', '')
        self.phone_number = user_data.get('phone_number', '')
        self.email = user_data.get('email', '')
        self.profile_picture = user_data.get('profile_picture', '')

    def __str__(self):
        return f"User(id={self.id}, firstname='{self.firstname}', lastname='{self.lastname}', username='{self.username}')"
