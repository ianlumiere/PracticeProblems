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

-- 4 most recent row for a customer
SELECT 
    s.*
FROM Subscribers s
WHERE s.date = (
    SELECT 
        MAX(s2.date) 
    FROM Subscribers s2 
    WHERE s2.customer_id = s.customer_id
    )

-- 5 get duplicate rows for single value
SELECT
    order_id,
    COUNT(order_id)
FROM orders
GROUP BY order_id
HAVING COUNT(order_id) > 1

-- 6 get duplicate rows for entire rows
SELECT
    order_id,
    product_id,
    COUNT(*)
FROM orders
GROUP BY order_id, product_id
HAVING COUNT(*) > 1

-- 7 rank salaries
SELECT
    full_name,
    salary,
    RANK() OVER (ORDER BY salary) AS 'salary_rank'
FROM employees

-- 8 get second highest salary for each department
WITH rankings AS (
    SELECT
        full_name,
        dept_id,
        salary,
        RANK() OVER (
            PARTITION BY dept_id
            ORDER BY salary
        ) AS 'salary_rank'
    FROM employees
)
SELECT
    *
FROM rankings r
WHERE salary_rank = 2