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

## WHERE and HAVING

WHERE Clause is used to filter the records from the table or used while joining more than one table.Only those records will be extracted who are satisfying the specified condition in WHERE clause. WHERE can be used in SELECT, UPDATE, and DELETE. 

HAVING Clause is used to filter the records from the groups based on the given condition in the HAVING Clause. Those groups who will satisfy the given condition will appear in the final result. HAVING Clause can only be used 
with SELECT statement. 

A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. A query can contain both a WHERE clause and a HAVING clause. 

WHERE Clause vs HAVING Clause
1.	WHERE Clause is used to filter the records from the table based on the specified condition.	
    HAVING Clause is used to filter record from the groups based on the specified condition.
2.	WHERE Clause can be used without GROUP BY Clause	
    HAVING Clause cannot be used without GROUP BY Clause
3.	WHERE Clause implements in row operations	
    HAVING Clause implements in column operation
4.	WHERE Clause cannot contain aggregate function	
    HAVING Clause can contain aggregate function
5.	WHERE Clause can be used with SELECT, UPDATE, DELETE statement.	
    HAVING Clause can only be used with SELECT statement.
6.	WHERE Clause is used before GROUP BY Clause	
    HAVING Clause is used after GROUP BY Clause
7.	WHERE Clause is used with single row function like UPPER, LOWER etc.	
    HAVING Clause is used with multiple row function like SUM, COUNT etc.

## Comments
- `-- can be added to the end of the line`
- `# this will make the whole line a comment`
- `/* this can be a multi line comment */`

## General Notes

- Multiple SQL statements must be separated by `;`.
- SQL is case insensitive.
- All extra whitespace in a SQL statement is ignored, so format how you like it.
- SQL is 0 indexed