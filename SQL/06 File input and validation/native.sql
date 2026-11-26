-- The runner imports the one-column CSV as readings(raw TEXT).
WITH cleaned AS (SELECT trim(raw) AS value FROM readings),
digits AS (
    SELECT value, CASE WHEN substr(value,1,1) IN ('+', '-')
          THEN substr(value,2) ELSE value END AS magnitude FROM cleaned
), typed AS (
    SELECT CASE WHEN magnitude <> '' AND magnitude NOT GLOB '*[^0-9]*'
           THEN cast(value AS integer) END AS x FROM digits
)
SELECT count(x), sum(x), min(x), max(x), count(*) - count(x) FROM typed;
