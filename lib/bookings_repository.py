from lib.bookings import Bookings
from lib.spaces import Spaces

class BookingsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_space_id(self, month):
        space_id = self._connection.execute('SELECT spaces_id FROM bookings WHERE booked_month = %s', [month])
        if len(space_id) == 0:
            return False
        else:
            return space_id[0]['spaces_id']

    def find_available_spaces(self, month):
        space_id = self.find_space_id(month)
        if space_id == False:
            spaces = []
            rows = self._connection.execute('SELECT * FROM spaces')
            for row in rows:
                item = Spaces(row['id'], row['title'], row['description'], row['email_address'], row['price_per_night'], row['user_id'])
                spaces.append(item)
            return spaces
        else:
            spaces = []
            rows = self._connection.execute('SELECT DISTINCT (spaces.id), spaces.title, spaces.description, spaces.email_address, spaces.price_per_night, spaces.user_id FROM spaces FULL OUTER JOIN bookings ON spaces.id = bookings.spaces_id WHERE spaces.id != %s ORDER BY spaces.id', [space_id])
            for row in rows:
                item = Spaces(row['id'], row['title'], row['description'], row['email_address'], row['price_per_night'], row['user_id'])
                spaces.append(item)
            return spaces