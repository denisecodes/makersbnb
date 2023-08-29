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
