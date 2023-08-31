import pytest
from lib.user_parameters_validator import UserParametersValidator

"""
With a valid first_name, last_name, email_address, user_password
It is valid
"""
def test_is_valid():
    validator = UserParametersValidator("TestName", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator.is_valid() == True

"""
With a blank first name or None first name
It is not valid
"""

def test_is_not_valid_with_incorrect_first_name():
    validator1 = UserParametersValidator("", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator1.is_valid() == False
    validator2 = UserParametersValidator(None, "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator2.is_valid() == False

"""
With a blank last name or None last name
It is not valid
"""

def test_is_not_valid_with_incorrect_last_name():
    validator1 = UserParametersValidator("TestName", "", "test@example.com", "testanimal123!!!")
    assert validator1.is_valid() == False
    validator2 = UserParametersValidator("TestName", None, "test@example.com", "testanimal123!!!")
    assert validator2.is_valid() == False

"""
With a blank email address or None email address
It is not valid
"""

def test_is_not_valid_with_incorrect_email_address():
    validator1 = UserParametersValidator("TestName", "TestSurname", "", "testanimal123!!!")
    assert validator1.is_valid() == False
    validator2 = UserParametersValidator("TestName", "TestSurname", None, "testanimal123!!!")
    assert validator2.is_valid() == False

"""
With a blank password or None password
It is not valid
"""

def test_is_not_valid_with_incorrect_password():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@email.com", "")
    assert validator1.is_valid() == False
    validator2 = UserParametersValidator("TestName", "TestSurname","test@email.com", None)
    assert validator2.is_valid() == False

"""
With invalid parameters
Produces errors
"""

def test_errors():
    validator1 = UserParametersValidator("", "", "", "")
    assert validator1.generate_errors() == [
        "First name must not be blank",
        "Last name must not be blank",
        "Email address must not be blank",
        "Password must not be blank"
    ]


def test_get_valid_first_name_if_first_name_is_valid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator1.get_valid_first_name() == "TestName"


def test_get_valid_first_name_refuses_if_invalid():
    validator1 = UserParametersValidator("", "TestSurname", "test@example.com", "testanimal123!!!")
    with pytest.raises(ValueError) as err:
        validator1.get_valid_first_name()
    assert str(err.value) == "Cannot get valid first name"

def test_get_valid_last_name_if_last_name_is_valid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator1.get_valid_last_name() == "TestSurname"

def test_get_valid_last_name_refuses_if_invalid():
    validator1 = UserParametersValidator("TestName", "", "test@example.com", "testanimal123!!!")
    with pytest.raises(ValueError) as err:
        validator1.get_valid_last_name()
    assert str(err.value) == "Cannot get valid last name"

def test_get_valid_email_address_if_email_address_is_valid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator1.get_valid_email_address() == "test@example.com"

def test_get_valid_email_address_refuses_if_invalid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "", "testanimal123!!!")
    with pytest.raises(ValueError) as err:
        validator1.get_valid_email_address()
    assert str(err.value) == "Cannot get valid email address"

def test_get_valid_user_password_if_user_password_is_valid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@example.com", "testanimal123!!!")
    assert validator1.get_valid_user_password() == "testanimal123!!!"

def test_get_valid_user_password_refuses_if_user_password_invalid():
    validator1 = UserParametersValidator("TestName", "TestSurname", "test@example.com", "")
    with pytest.raises(ValueError) as err:
        validator1.get_valid_user_password()
    assert str(err.value) == "Cannot get valid password"