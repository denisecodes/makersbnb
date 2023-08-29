from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection
        
    def validate_login(self, email_address, user_password):
        rows = self.connection.execute('SELECT * FROM users WHERE email_address = (%s) AND user_password = (%s)', [email_address, user_password])
        row = rows[0]
        print(row)

    # def validate_login(self, email_address, user_password):
    #     count = self.connection.execute('SELECT COUNT(id) AS existing_row_count FROM users WHERE email_address = (%s) AND user_password = (%s)', [email_address, user_password])
    #     print(count)