-- lists the number of records with the same score
SELECT score, COUNT(score)
FROM second_table
GROUP BY score AS number
HAVING COUNT(score) >1
ORDER BY score DESC;
