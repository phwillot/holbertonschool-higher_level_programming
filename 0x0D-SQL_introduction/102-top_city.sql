-- Displays the top 3 of cities temperature
-- during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = '8' OR month = '9'
