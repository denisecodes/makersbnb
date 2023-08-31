from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection
        

    def validate_login(self, email_address, user_password):
        count = self.connection.execute(
            'SELECT COUNT(id) FROM users WHERE email_address = (%s) AND user_password = (%s)', [email_address, user_password])
        value = count[0]["count"]
        if value == 1:
            return True 
        else: 
            return False