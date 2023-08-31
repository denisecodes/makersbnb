class UserParametersValidator:
    def __init__(self, first_name, last_name, email_address, user_password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_password = user_password

    def is_valid(self):
        if not self._is_first_name_valid():
            return False
        if not self._is_last_name_is_valid():
            return False
        if not self._is_email_address_is_valid():
            return False
        if not self._is_user_password_is_valid():
            return False
        else:
            return True

    def generate_errors(self):
        errors = []
        if not self._is_first_name_valid():
            errors.append("First name must not be blank")
        if not self._is_last_name_is_valid():
            errors.append("Last name must not be blank")
        if not self._is_email_address_is_valid():
            errors.append("Email address must not be blank")
        if not self._is_user_password_is_valid():
            errors.append("Password must not be blank")
        return errors

    def get_valid_first_name(self):
        if not self._is_first_name_valid():
            raise ValueError("Cannot get valid first name")
        return self.first_name

    def get_valid_last_name(self):
        if not self._is_last_name_is_valid():
            raise ValueError("Cannot get valid last name")
        return self.last_name

    def get_valid_email_address(self):
        if not self._is_email_address_is_valid():
            raise ValueError("Cannot get valid email address")
        return self.email_address

    def get_valid_user_password(self):
        if not self._is_user_password_is_valid():
            raise ValueError("Cannot get valid password")
        return self.user_password

    def _is_first_name_valid(self):
        if self.first_name is None or self.first_name == "":
            return False
        else:
            return True

    def _is_last_name_is_valid(self):
        if self.last_name is None or self.last_name == "":
            return False
        else:
            return True

    def _is_email_address_is_valid(self):
        if self.email_address is None or self.email_address == '':
            return False
        else:
            return True
        
    def _is_user_password_is_valid(self):
        if self.user_password is None or self.user_password == '':
            return False
        else:
            return True