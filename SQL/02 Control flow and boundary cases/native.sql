WITH readings(x) AS (VALUES (-4), (0), (5), (12), (18), (25), (31)),
labelled AS (
    SELECT CASE WHEN x <= 0 THEN 0 WHEN x < 20 THEN 1 ELSE 2 END AS band
    FROM readings
)
SELECT count(*) FROM labelled GROUP BY band ORDER BY band;
