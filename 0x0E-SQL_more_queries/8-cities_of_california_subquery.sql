-- lists all the cities of California
-- Results must be sorted in ascending order by cities.id

SELECT name
FROM hbtn_0d_usa.states
WHERE name = 'California'
ORDER BY id ASC;
