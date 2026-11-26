WITH readings(pos, x) AS (VALUES (1,2), (2,4), (3,8), (4,1), (5,3), (6,7)),
rolling AS (
    SELECT pos, avg(x) OVER w AS centre, count(*) OVER w AS size
    FROM readings WINDOW w AS (ORDER BY pos ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
)
SELECT centre FROM rolling WHERE size = 3 ORDER BY pos;
