-- creates the table id_not_null on the MySQL server
-- should have id INT with the default value 1
-- name VARCHAR(256)
-- If the table id_not_null already exists, your script should not fail

create table if not exists id_not_null(
	id int DEFAULT 1,
	name varchar(256) not null);
