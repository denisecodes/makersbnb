from lib.spaces import Spaces

def test_initial():
    space1 = Spaces(1, 'test title', 'test description', 'test email', 100, 11)
    assert space1.id == 1
    assert space1.title == 'test title'
    assert space1.description == 'test description'
    assert space1.email_address == 'test email'
    assert space1.price_per_night == 100
    assert space1.user_id == 11

def test_two_spaces_are_equal():
    space1 = Spaces(1, 'test title', 'test description', 'test email', 100, 11)
    space2 = Spaces(1, 'test title', 'test description', 'test email', 100, 11)
    assert space1 == space2