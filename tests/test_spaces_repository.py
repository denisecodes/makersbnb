from lib.spaces import Spaces
from lib.spaces_repository import SpacesRepository

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/seed_spaces.sql')
    repository = SpacesRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Spaces(1, 'Cornwall', 'Nice Cottage', 'email1@gmail.com', 1),
    Spaces(2, 'Manchester', 'Vibrant 2 Bedroom Aparment in Central Manchester', 'email2@gmail.com', 2),
    Spaces(3, 'Dorset', 'Lovely 5 Bedroom Mansion', 'email3@gmail.com', 3),
    Spaces(4, 'Lake District', 'Cosy Cabin with Jacuzzi', 'email4@gmail.com', 4),
    Spaces(5, 'Brighton', 'Seaside Studio Flat', 'email5@gmail.com', 5),
    Spaces(6, 'London', 'Semi Detached 3 Bedroom House', 'email6@gmail.com', 6)

    ]