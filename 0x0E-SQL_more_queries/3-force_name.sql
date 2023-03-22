-- creates the table force_name on the MySQL server.
-- should id INT
-- should have name VARCHAR(256) can’t be null
-- If the table force_name already exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name(
id int,
name varchar(256) not null);
