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

-- 9 nest the previous query directly instead of WITH AS
SELECT
    *
FROM (
    SELECT
        full_name,
        dept_id,
        salary,
        RANK() OVER (
            PARTITION BY dept_id
            ORDER BY salary
        ) AS 'salary_rank'
    FROM employees
) r
WHERE salary_rank = 2

-- 10 rank scores where there are no gaps between ranks and ties are allowed
SELECT
    score,
    DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores

-- 11 get the team size for each employee
SELECT
    employee_id,
    COUNT(employee_id) OVER(PARTITION BY team_id) AS team_size
FROM employee

-- 12 get the top 3 employees by salary by department with ties and no gaps
SELECT
    d.name,
    r.name,
    r.salary
FROM ( -- Doing a subquery instead of WITH AS
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS 'salary_rank'
    FROM Employee
) r
INNER JOIN Department d ON r.departmentId = d.id
WHERE r.salary_rank <= 3
ORDER BY d.name, r.salary DESC

-- 13 get active user list where an active user is someone who logs in 5 consecutive days
SELECT DISTINCT -- distinct because one user may login in 5 consecutive days multiple times
    l.id,
    a.name
FROM (
    SELECT
        id,
        login_date,
        LAG(login_date, 4) OVER (PARTITION BY id ORDER BY login_date) AS 'lag4'
    FROM Logins
) l
JOIN Accounts a ON a.id = l.id
WHERE DATEDIFF(day, lag4, login_date) = 4

-- 14 get each customer's order and add a percentage of total spend
SELECT
    first_name,
    order_details,
    round(order_cost / SUM(order_cost) OVER (PARTITION BY customer_id)::FLOAT * 100) AS 'percent_total_spend'
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id
