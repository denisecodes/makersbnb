DROP SEQUENCE IF EXISTS bookings_seq_id;
DROP TABLE IF EXISTS bookings;

CREATE SEQUENCE bookings_seq_id;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY, 
    booked_month TEXT, 
    spaces_id INT
);

INSERT INTO bookings (booked_month, spaces_id) VALUES ('March', 1);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('February', 3);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('November', 5);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('July', 1);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('March', 2);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('March', 4);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('November', 6);
INSERT INTO bookings (booked_month, spaces_id) VALUES ('November', 2);