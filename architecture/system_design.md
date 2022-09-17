# Architecture

## Technologies

### Python

#### REST

REST stands for Representational State Transfer. REST APIs must be stateless, meaning it can't store contexts between requests/can't remember who you are. Every request that is received must contain all of the info necessary to process that request. 

#### Requests

`GET`: reads a resource. Idempotent (every time you do it, you should get the same result, it does not change anything)

`POST`: used to create a new resource. Not idempotent because each time you make the request you are making a new resource.

`DELETE`: removes a resource. Idempotent because if you make the same request multiple times, it has the same request as making it once.

#### CRUD

Create (POST)

Read (GET)

Update (PUT)

Delete (DELETE)


### Databases

#### Relational Databases

`1 to 1`: Can be represented with two tables, think Person table and Contact_Info Table

`1 to Many`: Customer table and Orders table, the Orders table will have a Customer_ID FK in each row that links to the Customer table

`Many to Many`: You do not want this in a db, you should instead make a third table to connect the two that just has the FKs for each. Example is Students table and Classes table should have a Students_Classes table that has a row that has 2 FKs, one to Students table and one to the Classes table. 

`ER Diagram` is the box diagram that I like. Used more for the database side of things (defines tables and their relationships).

`UML Diagram` is used more commonly as a class diagram for software side of things (defines classes and their attributes and functions).

#### ODS (Operational Data Store)

Whatever an application uses to store its data, often changes constantly. Any data that impacts their day to day operations. For example, the DB that Amazon uses that stores every order that gets executed and the info related to it. Different from a data warehouse, which changes every night for instance. ODS is row oriented and can do lots of transactions in a second and can support lots of web servers that are hammering it. Oracle, Microsoft SQL Server, PostgreSQL, MySQL (all of these are OLTP Online Transaction Processing). Best for day to day data high transaction volume (like running an app, website, or a game).

#### Aurora

A MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. So this is an ODS. Competes with Oracle. Can have massive clusters (Doordash has a single cluster for 10TB and billions of rows, The Pokemon Company handles 300 logins per second, Dow Jones migrated from on-premise to Aurora with no disruption to service). ROW ORIENTED.

#### Redshift

Makes it simple and cost effective to run high performance queries on petabytes of semi-structured and structured data so that you can build powerful reports and dashboards using QuickSight or other business intelligence tools. Intuit uses Redshift for business intelligence. Used for querying large data sets quickly. (OLAP Online Analytics Processing). Better for analytics. Very expensive, great for massive processing jobs (can do huge parallel processing because has lots of available CPUs). COLUMN ORIENTED (COLUMNAR).

#### Spectrum

Serverless. Queries S3. More control over performance because it uses the redshift cluster size. Uses virtual table from glue catalog when querying S3. Use this for queries closely tied to a Redshift DW, can also be used to join data between S3 and Redshift and load the results into Redshift. Cheaper than Redshift because storage in S3 is cheaper and has an ephemeral compute. There is overhead cost, but that can be recouped if you do a giant query and fire up lots of EC2s for a short period of time. Can read data from S3 and transform it and then load it into Redshift. Can also be used for some ad hoc needs.

#### Athena

Serverless. Queries S3. Uses pooled resources provided by AWS, so less control over performance than Spectrum. Uses virtual table from glue catalog when querying S3. Use if all your data is in S3 and you do not want to analyze Redshift data.

#### Data Warehouse

`Data Warehouse`: Repository for structured, filtered data that has already been processed for a specific purpose. Use a very particular schema. Used for SQL DBs. Often used by analysts. More secure. Less flexible. 

`Data Mart`: A structure/access pattern specific to DW environments, used to retrieve client-facing data. The data mart is a subset of the data warehouse and is usually oriented to a specific business line or team.

#### Data Lake

`Data Lake`: Vast pool of raw data, purpose of which is not defined. Usually relates to a particular part of the business. Schemaless. Similar to non-relational NoSQL DBs. Often used by data scientists (usually requires more knowledge to use than a DW). Less secure. More flexible. In general, data lakes are good for analyzing data from different, diverse sources from which initial data cleansing can be problematic. Good for IoT and ML.

`Data Ocean`: Like a data lake but applies to the entire scope of the business.

`Data Reservoir`: Partly filtered part of the data lake that has been made ready for consumption.

#### Data Lakehouse

A data lakehouse is a new, open data management architecture that combines the flexibility, cost-efficiency, and scale of data lakes with the data management and ACID transactions of data warehouses, enabling business intelligence (BI) and machine learning (ML) on all data.

#### ACID

`Atomicity`: transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single unit, which either succeeds completely or fails completely, meaning if any of the statements in a transaction fail, the entire transaction fails and the db is left unchanged. Must guarantee atomicity in each situation including power failures, errors, and crashes. Prevents updates from occurring only partially.

`Consistency`: ensures that a transaction can only bring the db from one valid state to another, maintaining db invariants. Any data written must be valid according to all defined rules, including constraints, cascades, and triggers.

`Isolation`: transactions are often executed concurrently. Isolation ensures that concurrent execution of transactions leaves the db in the same state that would have been obtained if the transactions were executed sequentially.

`Durability`: once a transaction is committed, it will remain committed even in a system failure. Usually means completed transactions or effects are recorded in non-volatile memory.

#### Data Modeling

Data modeling is the method of documenting complex software design as a diagram so that anyone can easily understand. It is a conceptual representation of data objects that are associated between various data objects and the rules.

#### ETL vs ELT

ELT is better for data lakes because you want to store the raw data, can also go back and do transformations in different ways (might not know the transformations in advance, so just load it first before transforming it). Can also move data more quickly doing ELT. Can also load it and then transform it 2 different ways instead of doing one before loading it.

#### Data Normalization

Repeating for order data city info may be best in order table instead of creating an address table. You need to determine what level of normalization you want. Normalization is the technique to order data into tables to reduce redundancy. Data normalization can slow down updates because there are more tables to update, also creates longer task because there are more tables to join.

#### The Difference Between Data and Big Data Analytics

Prior to the invention of Hadoop, the technologies underpinning modern storage and compute systems were relatively basic, limiting companies mostly to the analysis of "small data." Even this relatively basic form of analytics could be difficult, though, especially the integration of new data sources. With traditional data analytics, which relies on the use of relational databases (like SQL databases), made up of tables of structured data, every byte of raw data needs to be formatted in a specific way before it can be ingested into the database for analysis. This often lengthy process, commonly known as extract, transform, load (or ETL) is required for each new data source. The main problem with this 3-part process and approach is that it’s incredibly time and labor intensive. 

Once data was inside the database, though, in most cases it was easy enough for data analysts to query and analyze. But then along came the Internet, eCommerce, social media, mobile devices, marketing automation, Internet of Things (IoT) devices, etc., and the size, volume, and complexity of raw data became too much for all but a handful of institutions to analyze in the normal course of business.

Big data analytics is the often complex process of examining large and varied data sets - or big data - that has been generated by various sources such as eCommerce, mobile devices, social media and the Internet of Things (IoT). It involves integrating different data sources, transforming unstructured data into structured data, and generating insights from the data using specialized tools and techniques that spread out data processing over an entire network. The amount of digital data that exists is growing at a fast pace, doubling every two years. Big data analytics is the solution that came with a different approach for managing and analyzing all of these data sources. While the principles of traditional data analytics generally still apply, the scale and complexity of big data analytics required the development of new ways to store and process the petabytes of structured and unstructured data involved. The demand for faster speeds and greater storage capacities created a technological vacuum that was soon filled by new storage methods, such as data warehouses and data lakes, and nonrelational databases like NoSQL, as well as data processing and data management technologies and frameworks, such as open source Apache Hadoop, Spark, and Hive. Big data analytics takes advantage of advanced analytic techniques to analyze really big data sets that include structured, semi-structured and unstructured data, from various sources, and in different sizes from terabytes to zettabytes.

The Most Common Data Types Involved in Big Data Analytics Include: Web, Text, Time and location, Real-time media, Smart grid and sensor, Social network, Linked, and Network.

Big data analytics helps organizations harness their data and use advanced data science techniques and methods, such as natural language processing, deep learning, and machine learning, uncovering hidden patterns, unknown correlations, market trends and customer preferences, to identify new opportunities and make more informed business decisions.

Advantages of Using Big Data Analytics Include: Cost reduction, Improved decision making, New products and services, Fraud detection.

#### Apache Hadoop

High Availability Distributed Object Oriented Platform (HADOOP). Does Map Reduce.  High availability via parallel distribution of object-oriented tasks. Apache Hadoop is an open source, Java-based software platform that manages data processing and storage for big data applications. The platform works by distributing Hadoop big data and analytics jobs across nodes in a computing cluster, breaking them down into smaller workloads that can be run in parallel. Hadoop isn’t a solution for data storage or relational databases. Instead, its purpose as an open-source framework is to process large amounts of data simultaneously in real-time.

#### Apache Spark

Is meant to solve the problem created by map reduce. Map reduce takes a computation on petabytes of data and breaks it up by parallelizing it and then stitching the small answers back together to get an answer to the big computation that was too big to execute. The problem is map reduce is hard to code (very tedious, writing a lot of the same things over again), so spark (written in scala), is a library that makes it easier to do the map reduce operation. PySpark is just Spark in python and is very similar to Pandas.

#### Hadoop vs Spark

Both widely used open-source frameworks for big data architectures. Each framework contains an extensive ecosystem of open-source technologies that prepare, process, manage and analyze big data sets. Spark is a Hadoop enhancement to MapReduce. The primary difference between Spark and MapReduce is that Spark processes and retains data in memory for subsequent steps, whereas MapReduce processes data on disk. As a result, for smaller workloads, Spark’s data processing speeds are up to 100x faster than MapReduce. Furthermore, as opposed to the two-stage execution process in MapReduce, Spark creates a Directed Acyclic Graph (DAG) to schedule tasks and the orchestration of nodes across the Hadoop cluster. This task-tracking process enables fault tolerance, which reapplies recorded operations to data from a previous state.

What is Apache Hadoop?

Apache Hadoop is an open-source software utility that allows users to manage big data sets (from gigabytes to petabytes) by enabling a network of computers (or “nodes”) to solve vast and intricate data problems. It is a highly scalable, cost-effective solution that stores and processes structured, semi-structured and unstructured data (e.g., Internet clickstream records, web server logs, IoT sensor data, etc.).

Benefits of the Hadoop framework include the following:

- Data protection amid a hardware failure
- Vast scalability from a single server to thousands of machines
- Real-time analytics for historical analyses and decision-making processes

What is Apache Spark?

Apache Spark — which is also open source — is a data processing engine for big data sets. Like Hadoop, Spark splits up large tasks across different nodes. However, it tends to perform faster than Hadoop and it uses random access memory (RAM) to cache and process data instead of a file system. This enables Spark to handle use cases that Hadoop cannot.

Benefits of the Spark framework include the following:

- A unified engine that supports SQL queries, streaming data, machine learning (ML) and graph processing
- Can be 100x faster than Hadoop for smaller workloads via in-memory processing, disk data storage, etc.
- APIs designed for ease of use when manipulating semi-structured data and transforming data

The Hadoop ecosystem

Hadoop supports advanced analytics for stored data (e.g., predictive analysis, data mining, machine learning (ML), etc.). It enables big data analytics processing tasks to be split into smaller tasks. The small tasks are performed in parallel by using an algorithm (e.g., MapReduce), and are then distributed across a Hadoop cluster (i.e., nodes that perform parallel computations on big data sets).

The Hadoop ecosystem consists of four primary modules:

- Hadoop Distributed File System (HDFS): Primary data storage system that manages large data sets running on commodity hardware. It also provides high-throughput data access and high fault tolerance.
- Yet Another Resource Negotiator (YARN): Cluster resource manager that schedules tasks and allocates resources (e.g., CPU and memory) to applications.
- Hadoop MapReduce: Splits big data processing tasks into smaller ones, distributes the small tasks across different nodes, then runs each task.
- Hadoop Common (Hadoop Core): Set of common libraries and utilities that the other three modules depend on.

The Spark ecosystem

Apache Spark, the largest open-source project in data processing, is the only processing framework that combines data and artificial intelligence (AI). This enables users to perform large-scale data transformations and analyses, and then run state-of-the-art machine learning (ML) and AI algorithms.

The Spark ecosystem consists of five primary modules:

- Spark Core: Underlying execution engine that schedules and dispatches tasks and coordinates input and output (I/O) operations.
- Spark SQL: Gathers information about structured data to enable users to optimize structured data processing.
- Spark Streaming and Structured Streaming: Both add stream processing capabilities. Spark Streaming takes data from different streaming sources and divides it into micro-batches for a continuous stream. Structured Streaming, built on Spark SQL, reduces latency and simplifies programming.
- Machine Learning Library (MLlib): A set of machine learning algorithms for scalability plus tools for feature selection and building ML pipelines. The primary API for MLlib is DataFrames, which provides uniformity across different programming languages like Java, Scala and Python.
- GraphX: User-friendly computation engine that enables interactive building, modification and analysis of scalable, graph-structured data.

Let’s take a closer look at the key differences between Hadoop and Spark in six critical contexts:

- Performance: Spark is faster because it uses random access memory (RAM) instead of reading and writing intermediate data to disks. Hadoop stores data on multiple sources and processes it in batches via MapReduce.
- Cost: Hadoop runs at a lower cost since it relies on any disk storage type for data processing. Spark runs at a higher cost because it relies on in-memory computations for real-time data processing, which requires it to use high quantities of RAM to spin up nodes.
- Processing: Though both platforms process data in a distributed environment, Hadoop is ideal for batch processing and linear data processing. Spark is ideal for real-time processing and processing live unstructured data streams.
- Scalability: When data volume rapidly grows, Hadoop quickly scales to accommodate the demand via Hadoop Distributed File System (HDFS). In turn, Spark relies on the fault tolerant HDFS for large volumes of data.
- Security: Spark enhances security with authentication via shared secret or event logging, whereas Hadoop uses multiple authentication and access control methods. Though, overall, Hadoop is more secure, Spark can integrate with Hadoop to reach a higher security level.
- Machine learning (ML): Spark is the superior platform in this category because it includes MLlib, which performs iterative in-memory ML computations. It also includes tools that perform regression, classification, persistence, pipeline construction, evaluation, etc.

Misconceptions about Hadoop and Spark

- Hadoop is cheap: Though it’s open source and easy to set up, keeping the server running can be costly. When using features like in-memory computing and network storage, big data management can cost up to $5,000 USD.
- Hadoop is a database: Though Hadoop is used to store, manage and analyze distributed data, there are no queries involved when pulling data. This makes Hadoop a data warehouse rather than a database.
- Hadoop does not help SMBs: “Big data” is not exclusive to “big companies”. Hadoop has simple features like Excel reporting that enable smaller companies to harness its power. Having one or two Hadoop clusters can greatly enhance a small company’s performance.
- Hadoop is hard to set up: Though Hadoop management is difficult at the higher levels, there are many graphical user interfaces (GUIs) that simplify programming for MapReduce.
- Spark is an in-memory technology: Though Spark effectively utilizes the least recently used (LRU) algorithm, it is not, itself, a memory-based technology.
- Spark always performs 100x faster than Hadoop: Though Spark can perform up to 100x faster than Hadoop for small workloads, according to Apache, it typically only performs up to 3x faster for large ones.
- Spark introduces new technologies in data processing: Though Spark effectively utilizes the LRU algorithm and pipelines data processing, these capabilities previously existed in massively parallel processing (MPP) databases. However, what sets Spark apart from MPP is its open-source orientation.

Hadoop use cases:

- Processing big data sets in environments where data size exceeds available memory
- Batch processing with tasks that exploit disk read and write operations
- Building data analysis infrastructure with a limited budget
- Completing jobs that are not time-sensitive
- Historical and archive data analysis

Spark use cases

- Dealing with chains of parallel operations by using iterative algorithms
- Achieving quick results with in-memory computations
- Analyzing stream data analysis in real time
- Graph-parallel processing to model data
- All ML applications

#### Apache Hive

Apache Hive was the early go-to solution for how to query SQL with Hadoop. This module emulates the behavior, syntax and interface of MySQL for programming simplicity. It’s a great option if you already heavily use Java applications as it comes with a built-in Java API and JDBC drivers. Hive offers a quick and straightforward solution for developers but it’s also quite limited as the software’s rather slow and suffers from read-only capabilities.

#### Snowflake Schema

A snowflake schema is a multi-dimensional data model that is an extension of a star schema, where dimension tables are broken down into subdimensions. Snowflake schemas are commonly used for business intelligence and reporting in OLAP data warehouses, data marts, and relational databases.

In a snowflake schema, engineers break down individual dimension tables into logical subdimensions. This makes the data model more complex, but it can be easier for analysts to work with, especially for certain data types.

It's called a snowflake schema because its entity-relationship diagram (ERD) looks like a snowflake. A snowflake schema diagram with a central fact table that connects to multiple dimensional tables and subdimensional tables via foreign keys.

Snowflake schemas vs. star schemas

Like star schemas, snowflake schemas have a central fact table which is connected to multiple dimension tables via foreign keys. However, the main difference is that they are more normalized than star schemas. Snowflake schemas offer more storage efficiency, due to their tighter adherence to high normalization standards, but query performance is not as good as with more denormalized data models. Denormalized data models like star schemas have more data redundancy (duplication of data), which makes query performance faster at the cost of duplicated data (less joins required).

Benefits of snowflake schemas

- Fast data retrieval
- Enforces data quality
- Simple, common data model for data warehousing

Drawbacks of snowflake schemas

- Lots of overhead upon initial setup
- Rigid data model
- High maintenance costs

#### DBT

DBT is within warehouse airflow, benefit is that you can get the result using sql. Builds based off of how you write sql files, self resolves what happens up and downstream, gives out of the box testing. Lets you write macros. Bridges gap between data analysts and engineers. Reduces barrier to entry to work with data pipelines.

#### Databricks

Apache tool used to work with Spark. Can use iPython Notebooks. All data, analytics, and AI in one platform. Multicloud and open source.
