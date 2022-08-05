SELECT
    d.name,
    COUNT(e.id) AS num_ee
FROM department d
LEFT JOIN employee e on d.id = e.dept_id
GROUP BY d.name
ORDER BY num_ee DESC, d.name -- this will order by the number of ee's from high to low, then by name alphabetically if num is tied

SELECT
    name
FROM Products
LIMIT 3 OFFSET 5; -- returns 3 rows starting from row 5

