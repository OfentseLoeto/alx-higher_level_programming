-- lists all the cities of California
-- Results must be sorted in ascending order by cities.id

SELECT id, name, cities.id
FROM states
WHERE name = California
ORDER BY cities.id;
