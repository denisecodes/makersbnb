-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255), 
    user_password VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Ellie', 'Priestley', 'email1@gmail.com', '12345');
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Emily', 'Cowan' 'email2@gmail.com', '56irf');
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Denise', 'Chan', 'email3@gmail.com', '348fj');
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Alina', 'Ermakova', 'email4@gmail.com', '03jff');
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Alex', 'Wilson', 'email5@gmail.com', '09cnm');
INSERT INTO users (first_name, last_name, email_address, user_password) VALUES ('Mohsin', 'Hafesji', 'email6@gmail.com', '98dfb');
