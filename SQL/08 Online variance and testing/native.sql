WITH observations(pos, x) AS (
    VALUES (1,1000000001.0), (2,1000000002.0), (3,1000000004.0), (4,1000000005.0)
), means AS (
    SELECT pos, avg(x) OVER (ORDER BY pos ROWS UNBOUNDED PRECEDING) AS centre FROM observations
)
SELECT avg((o.x - m.centre)*(o.x - m.centre))
FROM means m JOIN observations o ON o.pos <= m.pos GROUP BY m.pos ORDER BY m.pos;
