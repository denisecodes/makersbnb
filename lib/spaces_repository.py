from lib.spaces import Spaces

class SpacesRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Spaces(row['id'], row['title'], row['description'], row['email_address'], row['price_per_night'], row['user_id'])
            spaces.append(item)
        return spaces
    
    def create(self, space):
        # We can use RETURNING id after the placeholders in order to return id for finding page for specific spaces for logged in user
        self._connection.execute('INSERT INTO spaces (title, description, email_address, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s)', [space.title, space.description, space.email_address, space.price_per_night, space.user_id])
        return None