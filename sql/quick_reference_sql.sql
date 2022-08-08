-- 1
SELECT
    d.name,
    COUNT(e.id) AS num_ee
FROM department d
LEFT JOIN employee e on d.id = e.dept_id
GROUP BY d.name
ORDER BY num_ee DESC, d.name -- this will order by the number of ee's from high to low, then by name alphabetically if num is tied

-- 2
SELECT
    name
FROM Products
LIMIT 3 OFFSET 5; -- returns 3 rows starting from row 5

-- 3
WITH Stats AS (
SELECT
    area,
    CASE 
        WHEN opinion = 'rec' THEN 1
        ELSE -1
    END AS rec_value
FROM Reviews
),
Stats_Sum AS (
SELECT
    area,
    SUM(rec_value) AS rec_total
FROM Stats
GROUP BY area
)
SELECT
    area
FROM Stats_Sum
WHERE rec_total > 0
ORDER BY area
