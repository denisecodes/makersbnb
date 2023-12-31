class User:
    def __init__(self, first_name, last_name, email_address, user_password, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_password = user_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email_address}, {self.user_password})"
    
