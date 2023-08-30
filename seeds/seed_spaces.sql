DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_seq_id;

CREATE SEQUENCE spaces_seq_id;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    email_address TEXT,
    user_id INT
);

INSERT INTO spaces (title, description, email_address, user_id) VALUES ('Cornwall', 'Nice Cottage', 'email1@gmail.com', 1);
INSERT INTO spaces (title, description, email_address, user_id) VALUES ('Manchester', 'Vibrant 2 Bedroom Aparment in Central Manchester', 'email2@gmail.com', 2);
INSERT INTO spaces (title, description, email_address, user_id) VALUES ('Dorset', 'Lovely 5 Bedroom Mansion', 'email3@gmail.com', 3);
INSERT INTO spaces (title, description, email_address, user_id) VALUES ('Lake District', 'Cosy Cabin with Jacuzzi', 'email4@gmail.com', 4);
INSERT INTO spaces (title, description, email_address, user_id) VALUES ('Brighton', 'Seaside Studio Flat', 'email5@gmail.com', 5);
INSERT INTO spaces (title, description, email_address, user_id) VALUES ('London', 'Semi Detached 3 Bedroom House', 'email6@gmail.com', 6);