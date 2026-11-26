WITH temperatures(pos, celsius) AS (
    VALUES (1,-10), (2,0), (3,10), (4,20), (5,30)
)
SELECT 9.0 * celsius / 5 + 32 AS fahrenheit
FROM temperatures ORDER BY pos;
