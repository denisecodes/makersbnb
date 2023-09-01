from lib.bookings_repository import *

def test_find_spaces_not_booked_in_march(db_connection):
    db_connection.seed('seeds/seed_bookings.sql')
    db_connection.seed('seeds/seed_spaces.sql')
    repository = BookingsRepository(db_connection)
    available_spaces = repository.find_available_spaces('March')
    assert available_spaces == [
        Spaces(3, 'Dorset', 'Lovely 5 Bedroom Mansion', 'email3@gmail.com', 900, 3),
        Spaces(5, 'Brighton', 'Seaside Studio Flat', 'email5@gmail.com', 455, 5),
        Spaces(6, 'London', 'Semi Detached 3 Bedroom House', 'email6@gmail.com', 2250, 6)
    ]

def test_find_space_id_for_february(db_connection):
    db_connection.seed('seeds/seed_bookings.sql')
    db_connection.seed('seeds/seed_spaces.sql')
    repository = BookingsRepository(db_connection)
    space_id = repository.find_space_id('February')
    assert space_id == [3]

def test_find_spaces_for_january(db_connection):
    db_connection.seed('seeds/seed_bookings.sql')
    db_connection.seed('seeds/seed_spaces.sql')
    repository = BookingsRepository(db_connection)
    available_spaces = repository.find_available_spaces('January')
    assert available_spaces == [Spaces(1, 'Cornwall', 'Nice Cottage', 'email1@gmail.com', 200, 1),
    Spaces(2, 'Manchester', 'Vibrant 2 Bedroom Aparment in Central Manchester', 'email2@gmail.com', 150, 2),
    Spaces(3, 'Dorset', 'Lovely 5 Bedroom Mansion', 'email3@gmail.com', 900, 3),
    Spaces(4, 'Lake District', 'Cosy Cabin with Jacuzzi', 'email4@gmail.com', 349, 4),
    Spaces(5, 'Brighton', 'Seaside Studio Flat', 'email5@gmail.com', 455, 5),
    Spaces(6, 'London', 'Semi Detached 3 Bedroom House', 'email6@gmail.com', 2250, 6)
    ]