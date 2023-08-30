from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection
        
    # def validate_login(self, email_address, user_password):
    #     rows = self.connection.execute(
    #         'SELECT * FROM users WHERE email_address = (%s) AND user_password = (%s)', 
    #         [email_address, user_password])
    #     if rows == :
    #         return False 
    #     print(rows)
    #     # row = rows[0]
    #     # print(row)
    #     # current_user = User(row["id"], row["first_name"], row["last_name"], 
    #     #                     row["email_address"], row["user_password"])
    #     # return True


    def validate_login(self, email_address, user_password):
        count = self.connection.execute(
            'SELECT COUNT(id) FROM users WHERE email_address = (%s) AND user_password = (%s)', [email_address, user_password])
        print(count)
        value = count[0]["count"]
        print(value)
        if value == 1:
            return True 
        else: 
            return False