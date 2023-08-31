from lib.user_repository import * 
from lib.user import * 

"""
Test that when a user inputs correct email and password when #validate_login is called, returns True
"""

def test_check_login_is_true_for_valid_login(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    assert repository.validate_login('email1@gmail.com','12345') == True

"""
Test that when a user inputs incorrect email and password when #validate_login is called, returns False
"""

def test_check_login_is_false_for_invalid_login(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    assert repository.validate_login('random@gmail.com','12347') == False


    