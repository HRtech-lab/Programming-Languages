WITH RECURSIVE
values_to_test(n) AS (VALUES (0.0), (0.5), (2.0), (10.0), (25.0)),
bracket(n, lo, hi, step) AS (
    SELECT n, 0.0, max(1.0, n), 0 FROM values_to_test
    UNION ALL
    SELECT n,
           CASE WHEN ((lo+hi)/2)*((lo+hi)/2) < n THEN (lo+hi)/2 ELSE lo END,
           CASE WHEN ((lo+hi)/2)*((lo+hi)/2) < n THEN hi ELSE (lo+hi)/2 END,
           step + 1
    FROM bracket WHERE step < 55
)
SELECT CASE WHEN n = 0 THEN 0 ELSE (lo+hi)/2 END FROM bracket
WHERE step = 55 ORDER BY n;
