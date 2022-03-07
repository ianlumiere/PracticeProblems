# SQL NOTES

## Definitions

- `SQL`: Structured Query Language.
- `Database`: A collection of data stored in some organized fashion.
- `Database Management System (DBMS)`: The actual database software that creates and manipulates the container that is the database.
- `Table`: A structured list of data of a specific type. Always has a unique name. 
- `Schema`: Info about database and table layout and properties. The set of info that describes a table. Can also describe an entire database.
- `Column`: A single field in a table. All tables are made up of one or more columns.
- `Row`: A record in a table.
- `Primary Key`: A column (or set of columns) whose values uniquely identify every row in a table. Without a PK, updating or deleting specific rows becomes difficult and there is no guaranteed safe way to refer to the just the rows to be effected. Not required, but you should have them in every table.
    - No two rows can have the same PK
    - Every row must have a PK (no NULL values)
    - PKs should never be modified or updated
    - PK values should never be reused (if a row is deleted, its PK may NOT be assigned to a new row in the future)
- `Foreign Key`: A field (or collection of fields) in one table, that refers to the PK in another table.

## Keywords

- SELECT
- AS
- DISTINCT
- CONCAT() in MySQL, || in Postgres
- TRIM()
- RTRIM()
- LTRIM()
- CASE WHEN
- FROM
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CROSS JOIN
- WHERE
- HAVING
- LIKE
- IN
- GROUP BY
- ORDERY BY
- LIMIT OFFSET

## Super Query

```
SELECT
    p.id,
    p.price,
    p.name,
    p.type,
    CONCAT(p.origin_city, ' ', p.origin_state) AS 'product_origin_city_state',
    CASE
        WHEN p.price >= 10 THEN TRUE
        ELSE FALSE
    END AS 'big sale',
    o.order_id
FROM Products p
WHERE
    (price >= 5.49 OR
    price BETWEEN 1 AND 3) AND
    name != 'cherry' AND
    name IS NOT NULL XOR
    id NOT IN (0, 1, 2) AND
    name LIKE '%card_' -- This would get 'pokemon cards', but not 'pokemon card'
INNER JOIN Orders o ON p.name = o.name
ORDER BY price DESC, name
LIMIT 5, 2
```

## SELECT

Main purpose is to retrieve information from one or more tables. Data will always be returned in no order of any significance.

### DISTINCT

Only returns rows with distinct values. Applies to all named columns, not just the one it preceeds.

```
SELECT
    DISTINCT vend_id,
    price -- DISTINCT applies to this too!
FROM Products;
```

### LIMIT and OFFSET

You can use LIMIT to say how many rows you want max and OFFSET to tell it where to start. 
In MySQL, you can shorten it to `LIMIT 5, 3` where the OFFSET here would be 3.
NOTE: the first row is row 0, so OFFSET 1 will start at the second row.

```
SELECT
    vend_id,
    price
FROM Products
LIMIT 5 OFFSET 3; -- returns 5 rows starting at row 3
```

## Sorting Data

ORDER BY should be the last statement in the SELECT statement, aside from LIMIT.
ASC and DESC only apply to the column name it preceeds.

- ASC (the default)
    - A-Z
    - low to high (0-100)

- DESC
    - Z-A
    - high to low (100-0)

```
SELECT
    prod_id,
    prod_price,
    prod_name
FROM Products
ORDER BY prod_price DESC, prod_name; -- this will sort first by prod_price from highest price to lowest, then prod_name for any ties on price from A-Z
```

## WHERE

Use single quotes to delimit strings, not double quotes. Processes AND operators before OR operators

### MySQL Operators
Symbol | Function |
--- | --- |
`>` | Greater than operator
`>=` |	    Greater than or equal operator
`>=` |	    Greater than or equal operator		
`<`	  |      Less than operator		
`=`	      |  Equal operator	
`<>`, `!=` |	Not equal operator
`<=`	|    Less than or equal operator		
`<=>`	 |   NULL-safe equal to operator	
`+`	       | Addition operator		
`-`	       | Minus operator		
`-`	       | Change the sign of the argument			
`*`	       | Multiplication operator
`/`	   |     Division operator				
`DIV` |	Integer division
`%`, `MOD` |	Modulo operator				
`:=`	|    Assign a value		
`=`	     |   Assign a value (as part of a SET statement, or as part of the SET clause in an UPDATE statement)			
`AND`, `&&` |	Logical AND	
`OR`, `||` |	Logical OR	
`XOR` |	Logical XOR	
`IS` |	Test a value against a boolean		
`IS NOT` |	Test a value against a boolean		
`IS NOT NULL`, `NOT NULL` | value test		
`IS NULL`, `NULL` | value test		
`NOT`, `!` |	Negates value
`LIKE` |	Simple pattern matching	
`NOT LIKE` |	Negation of simple pattern matching	
`BETWEEN ... AND ...` |	Whether a value is within a range of values			
`NOT BETWEEN ... AND ...` |	Whether a value is not within a range of values		
`CASE` |	Case operator
`BINARY` |	Cast a string to a binary string				
`IN()` |	Whether a value is within a set of values	
`NOT IN()` |	Whether a value is not within a set of values		
`MEMBER OF()` |	Returns true (1) if first operand matches any element of JSON array passed as second operand, otherwise returns false (0)
`->`	|    Return value from JSON column after evaluating path; equivalent to JSON_EXTRACT().		
`->>`	 |   Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON_UNQUOTE(JSON_EXTRACT()).
`>>` | Right shift				
`<<`	|    Left shift	
`&`	     |   Bitwise AND		
`\|` |	Bitwise OR		
`^`	 |       Bitwise XOR	
`~` |	Bitwise inversion
`NOT REGEXP` |	Negation of REGEXP			
`REGEXP` |	Whether string matches regular expression		
`RLIKE` |	Whether string matches regular expression	

### WHERE vs HAVING

WHERE Clause is used to filter the records from the table or used while joining more than one table.Only those records will be extracted who are satisfying the specified condition in WHERE clause. WHERE can be used in SELECT, UPDATE, and DELETE. 

HAVING Clause is used to filter the records from the groups based on the given condition in the HAVING Clause. Those groups who will satisfy the given condition will appear in the final result. HAVING Clause can only be used 
with SELECT statement. 

A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. A query can contain both a WHERE clause and a HAVING clause. 

WHERE Clause | HAVING Clause |
--- | --- |
Used to filter the records from the table based on the specified condition.	| Used to filter record from the groups based on the specified condition.
Can be used without GROUP BY Clause | Cannot be used without GROUP BY Clause
Implements in row operations | Implements in column operation
Cannot contain aggregate function | Can contain aggregate function
Can be used with SELECT, UPDATE, DELETE statement. | Can only be used with SELECT statement.
Used before GROUP BY Clause | Used after GROUP BY Clause
Used with single row function like UPPER, LOWER etc. | Used with multiple row function like SUM, COUNT etc.

### LIKE

To use wildcards, the LIKE operator must be used. Wildcards can only be used with strings. Try to not overuse them. Try not to use them at the beginning of the search pattern because that will make it the slowest to process.

Symbol | Function |
--- | --- |
`%` | Match any number of occurrences of any character and also works for no characters.
`_` | Matches any single character, but will not match for no characters.

## Aggregate Functions

- `COUNT` counts how many rows are in a particular column.
- `SUM` adds together all the values in a particular column.
- `MIN` and `MAX` return the lowest and highest values in a particular column, respectively.
- `AVG` calculates the average of a group of selected values.

```
SELECT 
    AVG(price)
FROM Products;
```

## Calculated Fields

### Concatenating

Postgres:
```
SELECT
    vend_city || ' ' || vend_state AS 'vendor_city_state'
FROM Vendors;
```

MySQL:
```
SELECT
    CONCAT(origin_city, ' ', origin_state) AS 'origin_city_state',
FROM Products;
```

### Trimming

TRIM() removes whitespace on the left and right of the value
RTRIM() removes whitespace from the right of the value
LTRIM() removes whitespace to the left of the value

### Calculations

You can use `+`, `-`, `*`, `/` as mathematical operators in creating calculated fields.

```
SELECT
    prod_id,
    quantity,
    price,
    quantity * price AS total_value
FROM Products
```

## DATE Functions



## Ranking



## CASE Statements

The CASE statement goes through conditions and returns a value when the first condition is met (like an if-then-else statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause. If there is no ELSE part and no conditions are true, it returns NULL.

```
SELECT 
    OrderID, 
    Quantity,
    CASE
        WHEN Quantity > 30 THEN 'The quantity is greater than 30'
        WHEN Quantity = 30 THEN 'The quantity is 30'
        ELSE 'The quantity is under 30'
    END AS QuantityText
FROM OrderDetails;
```

## COALESCE

The COALESCE function returns the first non-NULL value in a given list. Unlike the ISNULL function, it can accept multiple expressions.

```
SELECT 
    ID, 
    Student,
    COALESCE(Email1, Email2, 'N/A') AS Primary_Email
FROM Students
ORDER BY ID
```

## JOIN

### CROSS JOIN vs FULL OUTER JOIN

A CROSS JOIN produces a cartesian product between the two tables, returning all possible combinations of all rows. It has no on clause because you're just joining everything to everything.

A FULL OUTER JOIN is a combination of a left outer and right outer join. It returns all rows in both tables that match the query's where clause, and in cases where the on condition can't be satisfied for those rows it puts null values in for the unpopulated fields.

## UNION

### UNION vs UNION ALL

UNION ALL keeps all of the records from each of the original data sets, UNION removes any duplicate records. UNION first performs a sorting operation and eliminates of the records that are duplicated across all columns before finally returning the combined data set.

## GROUP BY

Grouping lets you divide data into logical sets so that you can perform aggregate calculations on each group.

```
SELECT
    vend_id,
    COUNT(*) AS num_prods
FROM Products
GROUP BY vend_id
HAVING COUNT(*) >= 2; -- cannot just reference the alias
```

HAVING supports all of WHERE's operators.

## INSERT

```
INSERT INTO table_name (column1, column2, column3, ...) -- column naming not needed if you are inserting for every column
VALUES (value1, value2, value3, ...);
```

## DELETE

```
DELETE FROM table_name WHERE condition;
```

## UPDATE

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

## Correlated Subqueries

A correlated subquery is evaluated once for each row processed by the parent statement. The parent statement can be a SELECT, UPDATE, or DELETE statement. A correlated subquery is one way of reading every row in a table and comparing values in each row against related data. It is used whenever a subquery must return a different result or set of results for each candidate row considered by the main query. In other words, you can use a correlated subquery to answer a multipart question whose answer depends on the value in each row processed by the parent statement. Ex:

```
SELECT column1, column2, ....
FROM table1 outer
WHERE column1 operator
                    (SELECT column1, column2
                     FROM table2
                     WHERE expr1 = 
                               outer.expr2);
```

## Comments
- `-- can be added to the end of the line`
- `# this will make the whole line a comment`
- `/* this can be a multi line comment */`

## General Notes

- Multiple SQL statements must be separated by `;`.
- SQL is case insensitive.
- All extra whitespace in a SQL statement is ignored, so format how you like it.
- SQL is 0 indexed
- It is far quicker to perform calculations on the database server than it is to perform within the client.

## Interview Questions:
1. What is a Primary Key? 

A column (or set of columns) whose values uniquely identify every row in a table

2. What is a Foreign Key? 

A field (or collection of fields) in one table, that refers to the PK in another table.

3. List the different types of joins and why would you use any of them Have you used variables (either in programming or data base queries?)

MySQL:
INNER JOIN: Returns records that have matching values in both tables
LEFT JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
CROSS JOIN: Returns all records from both tables

4. Have you pivoted a table? 

Turns the table to the right.

5. Have you moved data between data bases?

No

6. If you need a task/script to run every day to get data from a system, how do you set it up?

Airflow. Some type of scheduled ingestion system.

7. What is the difference between char (char or character) and varchar? 

char stores only fixed-length character string data types whereas varchar stores variable-length string where an upper limit of length is specified.

8. What is indexing? Why is it done?

Indexes are used to retrieve data from the database more quickly than otherwise. The users cannot see the indexes, they are just used to speed up searches/queries. Note: Updating a table with indexes takes more time than updating a table without (because the indexes also need an update).

9. What is stored procedures? 

A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

10. Why would you normalize a table? 

Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. Normalization is the process of creating a maximally efficient relational database. Essentially, databases should be organized to decrease redundancy and avoid dependence anomalies.

- First Normal Form (1NF)
    - This initial set of rules sets the fundamental guidelines for keeping your database properly organized.
    - Remove any repeating groups of data (i.e. beware of duplicative columns or rows within the same table)
    - Create separate tables for each group of related data
    - Each table should have a primary key (i.e. a field that identifies each row with a non-null, unique value)

- Second Normal Form (2NF)
    - This next set of rules builds upon those outlined in 1NF.
    - Meet every rule from 1NF
    - Remove data that doesn’t depend on the table’s primary key (either move the data to the appropriate table or create a new table and primary key)
    - Foreign keys are used to identify table relationships

- Third Normal Form (3NF)
    - This set of rules takes those outlined in 1NF and 2NF a step further.
    - Meet every rule from 1NF and 2NF
    - Remove attributes that rely on other non-key attributes (i.e. remove columns that depend on columns that aren’t foreign or primary keys)

11. When would you normalize a dimension? Its advantages & disadvantages?

?