from lib.bookings import Bookings

def test_initial_bookings():
    booking1 = Bookings(1, 'January', 1)
    assert booking1.id == 1
    assert booking1.booked_month == 'January'
    assert booking1.spaces_id == 1

def test_equal_booking_objects():
    booking1 = Bookings(1, 'January', 1)
    booking2 = Bookings(1, 'January', 1)
    assert booking1 == booking2