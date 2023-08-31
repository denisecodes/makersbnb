Bookings table design:

Assuming that all spaces are available 365 days a year

table name: bookings
columns:
start date
end date
spaces_id (have this as a foreign key that refers to the spaces table)

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY, 
    start_date DATE, 
    end_date DATE, 
    spaces_id INT
);

INSERT INTO bookings (start_date, end_date, spaces_id) VALUES (2023-01-10, 2023-01-15, 1);
INSERT INTO bookings (start_date, end_date, spaces_id) VALUES (2023-02-01, 2023-02-22, 3);
INSERT INTO bookings (start_date, end_date, spaces_id) VALUES (2023-01-01, 2023-01-09, 5);
INSERT INTO bookings (start_date, end_date, spaces_id) VALUES (2023-01-17, 2023-01-20, 1);