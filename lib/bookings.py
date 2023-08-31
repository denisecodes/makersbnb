class Bookings:
    def __init__(self, id, booked_month, spaces_id):
        self.id = id
        self.booked_month = booked_month
        self.spaces_id = spaces_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__