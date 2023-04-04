-- lists all the cities of California
-- Results must be sorted in ascending order by cities.id

SELECT *
FROM cities.states
WHERE name = 'California'
ORDER BY cities.id ASC;
