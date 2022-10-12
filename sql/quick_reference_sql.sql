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
    WHERE s2.customer_id = s.customer_id)

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
        RANK() OVER (PARTITION BY dept_id ORDER BY salary) AS 'salary_rank'
    FROM employees)
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
        RANK() OVER (PARTITION BY dept_id ORDER BY salary) AS 'salary_rank'
    FROM employees) r
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
    FROM Employee) r
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
    FROM Logins) l
JOIN Accounts a ON a.id = l.id
WHERE DATEDIFF(day, lag4, login_date) = 4

-- 14 get each customer's order and add a percentage of total spend
SELECT
    first_name,
    order_details,
    ROUND(order_cost / SUM(order_cost) OVER (PARTITION BY customer_id)::FLOAT * 100) AS 'percent_total_spend'
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id

-- 15 get average distance per dollar
SELECT
    b.request_date,
    ROUND(ABS(b.dist_to_cost-b.avg_distance_to_cost)::DECIMAL, 2) AS 'mean_deviation'
FROM (
    SELECT
        a.request_date,
        a.dist_to_cost,
        AVG(a.dist_to_cost) OVER (PARTITION BY a.request_month) AS 'avg_distance_to_cost'
    FROM (
        SELECT *,
            to_char(request_date::date, 'YYYY-MM') AS 'request_month',
            (distance_to_travel/monetary_cost) AS 'distance_to_cost'
        FROM uber_request_logs) a
    ORDER BY request_date) b
GROUP BY b.request_date, b.dist_to_cost, b.avg_distance_to_cost
ORDER BY b.request_date

-- 16 get top 5 percent of fraud scores per state
-- NOTE NTILE() gives you buckets, NTILE(10) gives you 10 buckets, NTILE(25) gives you 4 buckets
SELECT
    *
FROM (
    SELECT
        *,
        NTILE(100) OVER (PARTITION BY state ORDER BY fraud_score DESC) AS 'percentile'
    FROM fraud_score) a
WHERE percentile <=5 -- This will get top 5 percent!

-- 17 get year over year growth for number of hosts
SELECT
    year,
    cur_year_host,
    prev_year_host,
    ROUND(((cur_year_host - prev_year_host)/(CAST(prev_year_host AS numeric)))*100) AS 'estimated_growth'
FROM (
    SELECT
        year,
        cur_year_host,
        LAG(cur_year_host, 1) OVER (ORDER BY year) AS prev_year_host -- stores the number of hosts for the previous year
    FROM (
        SELECT
            extract(year FROM host_since::date) AS 'year',
            COUNT(id) AS 'cur_year_host' -- this will count the number of hosts for each year
        FROM airbnb_search_details
        WHERE host_since IS NOT NULL
        GROUP BY extract(year FROM host_since::date)
    ) t1
) t2

-- 18 convert date to YYYY-MM
SELECT
    to_char(CAST(created_at AS date), 'YYYY-MM') AS 'year_month'
FROM orders

-- 19 calculate month over month percent change in revenue
SELECT
    to_char(created_at::date, 'YYYY-MM') AS year_month,
    ROUND((SUM(value) - LAG(SUM(value), 1) OVER (w)) / 
        LAG(SUM(value), 1) OVER (w) * 100, 2) AS revenue_diff
FROM transactions
GROUP BY year_month
WINDOW w AS (ORDER BY to_char(created_at::date, 'YYYY-MM')) -- this can be referenced above
ORDER BY year_month ASC

-- 20 calculate what percentage of users clicked the top 3 results
SELECT
    (COUNT(CASE WHEN position <= 3 has_clicked = 'yes' THEN b.search_id ELSE NULL END)::FLOAT /
    COUNT(*)) * 100 AS percentage
FROM results a
LEFT JOIN search_events b ON a.result_id = b.search_id

-- 21 bucket number of reviews into different labels
SELECT
    user_id,
    CASE
        WHEN num_reviews = 0 THEN 'new'
        WHEN num_reviews BETWEEN 1 AND 5 'starting' -- any count of 5 will hit starting and not active
        WHEN num_reviews BETWEEN 6 AND 10 'active' -- could overlap and do 5 instead of 6, but it is less clear
        WHEN num_reviews > 10 THEN 'very_active'
    END AS activity_level
FROM reviews
