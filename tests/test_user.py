from lib.user import *

"""
Initiallizing new user
"""

def test_new_user():
    new_user = User(1, "Alina", "Ermakova", "alalina@hmail.com", "123456789lala")
    assert new_user.id == 1
    assert new_user.first_name == "Alina"
    assert new_user.last_name == "Ermakova"
    assert new_user.email_address == "alalina@hmail.com"
    assert new_user.user_password == "123456789lala"

def test_equality_user():
    new_user1 = User(1, "Alina", "Ermakova", "alalina@hmail.com", "123456789lala")
    new_user2 = User(1, "Alina", "Ermakova", "alalina@hmail.com", "123456789lala")
    assert new_user1 == new_user2

def test_representation_user():
    new_user1 = User(1, "Alina", "Ermakova", "alalina@hmail.com", "123456789lala")
    assert str(new_user1) == "Alina Ermakova, alalina@hmail.com, 123456789lala"
