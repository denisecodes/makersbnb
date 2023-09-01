from lib.database_connection import DatabaseConnection
# Run this file to reset your database using the seeds
# ; pipenv run python seed_dev_database.py
connection = DatabaseConnection(test_mode=True)
connection.connect()
connection.seed("seeds/seed_spaces.sql")
connection.seed("seeds/seed_bookings.sql")
connection.seed("seeds/users.sql")
# Add your own seed lines below...  