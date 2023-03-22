-- creates the database hbtn_0d_usa 
-- and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail

create database if not exists hbtn_0d_usa;
create table hbtn_0d_usa.cities (
	PRIMARY KEY(`id`),
	`id` int not null AUTO_INCREMENT,
	`state_id` int not null,
	`name` varchar(256) not null,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`);
