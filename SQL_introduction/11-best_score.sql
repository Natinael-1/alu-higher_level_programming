-- Task: List records from second_table with score >= 10, ordered by score descending

-- Select score and name where score is 10 or higher
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
