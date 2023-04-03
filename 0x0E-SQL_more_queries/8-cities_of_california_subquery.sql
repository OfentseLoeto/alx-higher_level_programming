-- lists all the cities of California
-- Results must be sorted in ascending order by cities.id

SELECT * FROM hbtn_0d_usa.states
WHERE name = California
ORDER BY cities_id ASC;
