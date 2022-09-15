# Architecture

## Technologies


### Python

#### REST

REST stands for Representational State Transfer. REST APIs must be stateless, meaning it can't store contexts between requests/can't remember who you are. Every request that is received must contain all of the info necessary to process that request. 

#### Requests

GET: reads a resource. Idempotent (every time you do it, you should get the same result, it does not change anything)
POST: used to create a new resource. Not idempotent because each time you make the request you are making a new resource.
DELETE: removes a resource. Idempotent because if you make the same request multiple times, it has the same request as making it once.

#### CRUD

Create (POST)
Read (GET)
Update (PUT)
Delete (DELETE)


### Databases

#### Relational Databases

1 to 1: Can be represented with two tables, think Person table and Contact_Info Table
1 to Many: Customer table and Orders table, the Orders table will have a Customer_ID FK in each row that links to the Customer table
Many to Many: You do not want this in a db, you should instead make a third table to connect the two that just has the FKs for each. Example is Students table and Classes table should have a Students_Classes table that has a row that has 2 FKs, one to Students table and one to the Classes table. 

ER Diagram is the box diagram that I like. Used more for the database side of things (defines tables and their relationships).
UML Diagram is used more commonly as a class diagram for software side of things (defines classes and their attributes and functions).

#### ODS

ODS (Operational Data Store): is whatever an application uses to store its data, often changes constantly. Any data that impacts their day to day operations. For example, the DB that Amazon uses that stores every order that gets executed and the info related to it. Different from a data warehouse, which changes every night for instance. ODS is row oriented and can do lots of transactions in a second and can support lots of web servers that are hammering it. Oracle, Microsoft SQL Server, PostgreSQL, MySQL (all of these are OLTP Online Transaction Processing). Best for day to day data high transaction volume (like running an app, website, or a game).

#### Aurora

Aurora: A MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. So this is an ODS. Competes with Oracle. Can have massive clusters (Doordash has a single cluster for 10TB and billions of rows, The Pokemon Company handles 300 logins per second, Dow Jones migrated from on-premise to Aurora with no disruption to service). ROW ORIENTED.

#### Redshift

Redshift: Makes it simple and cost effective to run high performance queries on petabytes of semi-structured and structured data so that you can build powerful reports and dashboards using QuickSight or other business intelligence tools. Intuit uses Redshift for business intelligence. Used for querying large data sets quickly. (OLAP Online Analytics Processing). Better for analytics. Very expensive, great for massive processing jobs (can do huge parallel processing because has lots of available CPUs). COLUMN ORIENTED (COLUMNAR).

#### Spectrum

Spectrum: Serverless. Queries S3. More control over performance because it uses the redshift cluster size. Uses virtual table from glue catalog when querying S3. Use this for queries closely tied to a Redshift DW, can also be used to join data between S3 and Redshift and load the results into Redshift. Cheaper than Redshift because storage in S3 is cheaper and has an ephemeral compute. There is overhead cost, but that can be recouped if you do a giant query and fire up lots of EC2s for a short period of time. Can read data from S3 and transform it and then load it into Redshift. Can also be used for some ad hoc needs.

#### Athena

Athena: Serverless. Queries S3. Uses pooled resources provided by AWS, so less control over performance than Spectrum. Uses virtual table from glue catalog when querying S3. Use if all your data is in S3 and you do not want to analyze Redshift data.

#### DBT

DBT is within warehouse airflow, benefit is that you can get the result using sql. Builds based off of how you write sql files, self resolves what happens up and downstream, gives out of the box testing. Lets you write macros. Bridges gap between data analysts and engineers. Reduces barrier to entry to work with data pipelines.

#### Databricks

Apache tool used to work with Spark. Can use iPython Notebooks. All data, analytics, and AI in one platform. Multicloud and open source.

#### Spark

Is meant to solve the problem created by map reduce. Map reduce takes a computation on petabytes of data and breaks it up by parallelizing it and then stitching the small answers back together to get an answer to the big computation that was too big to execute. The problem is map reduce is hard to code (very tedious, writing a lot of the same things over again), so spark (written in scala), is a library that makes it easier to do the map reduce operation. PySpark is just Spark in python and is very similar to Pandas.

#### Data Warehouse

Data Warehouse: Repository for structured, filtered data that has already been processed for a specific purpose. Use a very particular schema. Used for SQL DBs. Often used by analysts. More secure. Less flexible. 
Data Mart: A structure/access pattern specific to DW environments, used to retrieve client-facing data. The data mart is a subset of the data warehouse and is usually oriented to a specific business line or team.

#### Data Lake

Data Lake: Vast pool of raw data, purpose of which is not defined. Usually relates to a particular part of the business. Schemaless. Similar to non-relational NoSQL DBs. Often used by data scientists (usually requires more knowledge to use than a DW). Less secure. More flexible. In general, data lakes are good for analyzing data from different, diverse sources from which initial data cleansing can be problematic. Good for IoT and ML.
Data Ocean: Like a data lake but applies to the entire scope of the business.
Data Reservoir: Partly filtered part of the data lake that has been made ready for consumption.

#### Data Lakehouse

PLACEHOLDER

#### ACID

Atomicity: transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single unit, which either succeeds completely or fails completely, meaning if any of the statements in a transaction fail, the entire transaction fails and the db is left unchanged. Must guarantee atomicity in each situation including power failures, errors, and crashes. Prevents updates from occurring only partially.
Consistency: ensures that a transaction can only bring the db from one valid state to another, maintaining db invariants. Any data written must be valid according to all defined rules, including constraints, cascades, and triggers.
Isolation: transactions are often executed concurrently. Isolation ensures that concurrent execution of transactions leaves the db in the same state that would have been obtained if the transactions were executed sequentially.
Durability: once a transaction is committed, it will remain committed even in a system failure. Usually means completed transactions or effects are recorded in non-volatile memory.

#### Data Modeling

Data modeling is the method of documenting complex software design as a diagram so that anyone can easily understand. It is a conceptual representation of data objects that are associated between various data objects and the rules.

#### ETL vs ELT

ELT is better for data lakes because you want to store the raw data, can also go back and do transformations in different ways (might not know the transformations in advance, so just load it first before transforming it). Can also move data more quickly doing ELT. Can also load it and then transform it 2 different ways instead of doing one before loading it.

#### Data Normalization

Repeating for order data city info may be best in order table instead of creating an address table. You need to determine what level of normalization you want. Normalization is the technique to order data into tables to reduce redundancy. Data normalization can slow down updates because there are more tables to update, also creates longer task because there are more tables to join.
