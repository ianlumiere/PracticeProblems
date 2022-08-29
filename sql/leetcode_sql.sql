create table employee
(
empid int AUTO_INCREMENT,
fname varchar(255),
lname varchar(255),
dept varchar(255),
project varchar(255),
address varchar(255),
dob date,
gender char(1),

primary key(empid)
);

insert into employee
(empid, fname,lname,dept,project,address,dob,gender)
values
(1, 'John', 'Smith','HR','P1','1600 Pennsylvania Ave.','1976-01-12','M'),
(2,'Ava', 'Muffinson','Admin','P2', '255 California St.','1968-02-05', 'F'),
(3, 'Cailin', 'Ninson','Account','P3', '10 Downing St.','1980-01-01', 'F'),
(4, 'Mike', 'Peterson','HR','P1', '1 Infinite Loop','1992-02-05', 'M'),
(5, 'Ian', 'Peterson','Admin','P2', '1 Infinite Loop', '1994-03-07', 'M');

create table employeeposition
(
empid int AUTO_INCREMENT,
position varchar(255),
dateofjoining date,
salary int,

foreign key(empid) references employee(empid)
);

insert into employeeposition
  (empid, position, dateofjoining, salary)
values
  (1, 'Manager', '2022-01-05',         500000),
  (2, 'Executive', '2022-02-05',            75000),
  (3, 'Manager', '2022-01-05',         90000),
  (2, 'Lead', '2022-02-05',   85000),
  (1, 'Executive', '2022-01-05',   300000);

-- We have two tables here
-- 1. employee - contains the demographic details of each of the employees at the firm.
-- 2. employeeposition - contains the details of their designation, doj, salary etc.

--1. Write a query to fetch the number of employees working in the ‘HR’ department.
SELECT
	COUNT(empid) AS hr_emps
FROM employee
WHERE dept = 'HR'

--2. Write a query to find all the employees whose salary is between 50000 to 100000.
-- employees is fname and lname
SELECT
	E.fname,
	E.lname
FROM employee E
INNER JOIN employeeposition ep ON e.empid = ep.empid
WHERE ep.salary >= 50000 and ep.salary <= 100000

--3. Write a query to find the fnames of employees that begin with ‘S’
SELECT
	fname
FROM employee
WHERE LOWER(fname) LIKE 's%'

--4. Write a query to fetch all employees who also hold the managerial position.
SELECT
	E.fname,
	E.lname,
	ep.position
FROM employee E
INNER JOIN employeeposition ep ON e.empid = ep.empid
WHERE ep.position = 'Manager' --could do LOWER and TRIM etc

--5. Write a query to retrieve duplicate records from a table.
SELECT
	orderid,
	count(orderid)
FROM Orders
Group BY Orderid
Having COUNT(OrderID) > 1

--6. Write a query to retrieve the list of employees working in the Admin department.
SELECT
	empid,
    Fname,
	LName
FROM employee
WHERE dept = 'Admin'

--7. Write a query to find the third-highest salary from the EmpPosition table.
--ranking is the better way, but this would do it for time purposes
SELECT
	ep.*
FROM employeeposition ep
ORDER BY salary DESC
LIMIT 1, 2

--8. Write a query to retrieve Departments who have less than 2 employees working in it.
WITH counts AS (
SELECT 
	dept,
COUNT(empid) AS department_count
FROM employee
GROUP BY dept
)

SELECT
	Department
FROM counts
WHERE department_count < 2

--9. Write a query to fetch top 3 records.
SELECT
	e.*,
	ep.*
FROM employee e
INNER JOIN employeeposition ep ON e.empid = ep.empid
ORDER BY ep.salary DESC
LIMIT 3

--10. Write a query to fetch the department-wise count of employees sorted by department’s count in ascending order.
WITH counts AS (
SELECT 
	dept,
COUNT(empid) AS department_count
FROM employee
GROUP BY dept
)

SELECT
	*
FROM counts
ORDER BY department_count ASC