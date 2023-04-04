-- creates the database hbtn_0d_usa 
-- and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE cities.hbtn_0d_usa (
	PRIMARY KEY (id),
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id),
	name VARCHAR(256) NOT NULL,
	REFERENCES hbtn_0d_usa.states(state_id);
