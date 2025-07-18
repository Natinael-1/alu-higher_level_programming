-- Task: Count how many records have the same score in second_table

-- Group by score and count records
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
