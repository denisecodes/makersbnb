from lib.spaces import Spaces

class SpacesRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Spaces(row['id'], row['title'], row['description'], row['email_address'], row['user_id'])
            spaces.append(item)
        return spaces