-- creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows.

CREATE TABLE IF NOT EXISTS hbtn_0c_0.student_pfmc.second_table (
	pk_username VARCHAR PRINARY KEY, id INT, name VARCHAR(256), score INT) 
	VALUES ('pk_Ofentse', 1, 'John', 10),
	       ('pk_Ofentse', 2, 'Alex', 3),
	       ('pk_Ofentse', 3, 'Bob', 14),
	       ('pk_Ofentse', 4, 'George', 8);
