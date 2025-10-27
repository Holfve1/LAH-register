DROP TABLE IF TABLE EXISTS attendees;
DROP SEQUENCE IF EXISTS attendees_id_seq;

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

