WITH ids(id) AS (VALUES ('A'), ('B'), ('C')),
readings(id, x) AS (VALUES ('A',3), ('B',8), ('A',5), ('C',2), ('B',NULL))
SELECT avg(r.x) FROM ids AS i LEFT JOIN readings AS r ON i.id = r.id
GROUP BY i.id ORDER BY i.id;
