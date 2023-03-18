-- lists all records of the table
-- list rows with name values
-- list by decending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
