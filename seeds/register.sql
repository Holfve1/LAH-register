DROP TABLE IF TABLE EXISTS register;
DROP SEQUENCE IF EXISTS register_id_seq;

CREATE SEQUENCE IF NOT EXISTS register_id_seq;
CREATE TABLE register (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255), 
    last_name VARCHAR(255),
    address VARCHAR(255)
    );

INSERT INTO register (first_name, last_name, address) VALUES ('Dave', 'Smith', 'Camden');
INSERT INTO register (first_name, last_name, address) VALUES ('Sam', 'Fell', 'Kilburn');
INSERT INTO register (first_name, last_name, address) VALUES ('John', 'Doe', 'Westminster');
INSERT INTO register (first_name, last_name, address) VALUES ('Sarah', 'Dunce', 'Elephant & Castle');

