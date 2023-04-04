-- lists all the cities of California
-- Results must be sorted in ascending order by cities.id

SELECT *
FROM cities
WHERE name = 'California'
AND id IS NULL OR id = ''
ORDER BY cities.id ASC;
