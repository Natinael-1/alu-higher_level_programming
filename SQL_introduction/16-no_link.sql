-- Task: List all records in second_table that have a non-empty name, ordered by score

-- Select non-null names ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
