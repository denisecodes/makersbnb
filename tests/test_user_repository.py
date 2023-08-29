from lib.user_repository import * 
from lib.user import * 

"""
Test that when a user inputs correct password, return True
"""

def test_check_password_and_username(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    assert repository.validate_login('email1@gmail.com','12345') == True