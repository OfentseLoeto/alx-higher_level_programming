-- creates the table unique_id on the MySQL server.
-- should have id INT with the default value 1 and must be unique
-- should have name VARCHAR(256)
-- And If the table unique_id already exists, your script should not fail

create table if not exists unique_id(
	id int DEFAULT 1 UNIQUE,
	name varchar(256) not null);
