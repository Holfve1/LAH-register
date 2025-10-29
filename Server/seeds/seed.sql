DROP TABLE IF EXISTS attendees;
DROP SEQUENCE IF EXISTS attendees_id_seq;

DROP TABLE IF EXISTS activities;
DROP SEQUENCE IF EXISTS activities_id_seq;

DROP TABLE IF EXISTS dates;
DROP SEQUENCE IF EXISTS dates_id_seq;

DROP TABLE IF EXISTS registrations;
DROP SEQUENCE IF EXISTS registrations_id_seq;


CREATE SEQUENCE IF NOT EXISTS attendees_id_seq;
CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255), 
    last_name VARCHAR(255),
    suburb VARCHAR(255)
    );

INSERT INTO attendees (first_name, last_name, suburb) VALUES ('Dave', 'Smith', 'Camden');
INSERT INTO attendees (first_name, last_name, suburb) VALUES ('Sam', 'Fell', 'Kilburn');
INSERT INTO attendees (first_name, last_name, suburb) VALUES ('John', 'Doe', 'Westminster');
INSERT INTO attendees (first_name, last_name, suburb) VALUES ('Sarah', 'Dunce', 'Elephant & Castle');


CREATE SEQUENCE IF NOT EXISTS activities_id_seq;
CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    activity VARCHAR(255)
    );

INSERT INTO activities (activity) VALUES ('Paintball');
INSERT INTO activities (activity) VALUES ('Salsa classes');
INSERT INTO activities (activity) VALUES ('Spanish school');


CREATE SEQUENCE IF NOT EXISTS dates_id_seq;
CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date DATE, 
    activity_id INT,
    );

INSERT INTO dates (date, activity_id) VALUES ('2025-05-03', 1);
INSERT INTO dates (date, activity_id) VALUES ('2025-05-05', 2);
INSERT INTO dates (date, activity_id) VALUES ('2025-06-11', 2);
INSERT INTO dates (date, activity_id) VALUES ('2025-07-15', 3);
INSERT INTO dates (date, activity_id) VALUES ('2025-09-21', 3);
INSERT INTO dates (date, activity_id) VALUES ('2025-10-26', 1);


CREATE SEQUENCE IF NOT EXISTS registrations_id_seq;
CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    attendee_id INT,
    date_id INT
    );

INSERT INTO activities (attendee_id, date_id) VALUES (1, 1);
INSERT INTO activities (attendee_id, date_id) VALUES (1, 2);
INSERT INTO activities (attendee_id, date_id) VALUES (1, 3);
INSERT INTO activities (attendee_id, date_id) VALUES (2, 1);
INSERT INTO activities (attendee_id, date_id) VALUES (3, 3);
INSERT INTO activities (attendee_id, date_id) VALUES (4, 2);
