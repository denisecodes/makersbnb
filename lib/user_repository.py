from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users;")
        users = []
        for row in rows:
            user = User(row['id'], row['first_name'], row['last_name'], row['email_address'], row['user_password'])
            users.append(user)
        return users
    
    def add(self, user):
        self._connection.execute("INSERT INTO users (first_name, last_name, email_address, user_password) VALUES (%s, %s, %s, %s)", [
            user.first_name, user.last_name, user.email_address, user.user_password
            ])
        return None
        
