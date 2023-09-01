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

"""
Get a list of users
"""
def test_all_users(db_connection):
    db_connection.seed("seeds/users.sql")
    user_repo = UserRepository(db_connection)
    users = user_repo.all()
    assert users == [
        User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345'),
        User(2, 'Emily', 'Cowan', 'email2@gmail.com', '56irf'),
        User(3, 'Denise', 'Chan', 'email3@gmail.com', '348fj'),
        User(4, 'Alina', 'Ermakova', 'email4@gmail.com', '03jff'),
        User(5, 'Alex', 'Wilson', 'email5@gmail.com', '09cnm'),
        User(6, 'Mohsin', 'Hafesji', 'email6@gmail.com', '98dfb')
    ]

"""
Add a new user
"""
def test_add_a_new_user(db_connection):
    db_connection.seed("seeds/users.sql")
    user_repo = UserRepository(db_connection)
    roberto = User("Roberto", "Quadraccia", 'roberto@gmail.com', "robertoisawesome123")
    user_repo.add(roberto)
    users = user_repo.all()
    assert users == [
        User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345'),
        User(2, 'Emily', 'Cowan', 'email2@gmail.com', '56irf'),
        User(3, 'Denise', 'Chan', 'email3@gmail.com', '348fj'),
        User(4, 'Alina', 'Ermakova', 'email4@gmail.com', '03jff'),
        User(5, 'Alex', 'Wilson', 'email5@gmail.com', '09cnm'),
        User(6, 'Mohsin', 'Hafesji', 'email6@gmail.com', '98dfb'),
        User(7, "Roberto", "Quadraccia", 'roberto@gmail.com', "robertoisawesome123")
    ]
    