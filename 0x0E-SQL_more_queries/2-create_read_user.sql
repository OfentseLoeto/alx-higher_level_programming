--  creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
--The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail

create database IF NOT EXISTS `hbtn_0d_02`;
create user IF NOT EXISTS 'user_0d_02'@'localhost'
IDENTIFIED BY 'user_0d_02_pwd';

GRANT SELECT 
PRIVILEGES ON `hbtn_0d_2`.* 
TO 'user_0d_2'@'localhost';
