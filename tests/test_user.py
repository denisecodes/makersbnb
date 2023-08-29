from lib.user import *

"""
Check that when initialising with certain properties 
We can access those properties 
"""

def test_initialises():
    user1 = User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345')
    assert user1.id == 1
    assert user1.first_name == 'Ellie'
    assert user1.last_name == 'Priestley'
    assert user1.email_address == 'email1@gmail.com'
    assert user1.user_password == '12345'


"""
Check that two instances with the same properties 
Are defined as equal 
"""

def test_equality():
    user1 = User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345')
    user2 = User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345')
    assert user1 == user2

"""
Check that instances format nicely 
"""

def test_format():
    user1 = User(1, 'Ellie', 'Priestley', 'email1@gmail.com', '12345')
    assert str(user1) == 'User(1, Ellie, Priestley, email1@gmail.com, 12345)'

    