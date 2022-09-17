# Architecture

## Python

### REST

REST stands for Representational State Transfer. REST APIs must be stateless, meaning it can't store contexts between requests/can't remember who you are. Every request that is received must contain all of the info necessary to process that request. 

### Requests

`GET`: reads a resource. Idempotent (every time you do it, you should get the same result, it does not change anything)

`POST`: used to create a new resource. Not idempotent because each time you make the request you are making a new resource.

`DELETE`: removes a resource. Idempotent because if you make the same request multiple times, it has the same request as making it once.

### CRUD

Create (POST)

Read (GET)

Update (PUT)

Delete (DELETE)


## Databases

### Relational Databases

`1 to 1`: Can be represented with two tables, think Person table and Contact_Info Table

`1 to Many`: Customer table and Orders table, the Orders table will have a Customer_ID FK in each row that links to the Customer table

`Many to Many`: You do not want this in a db, you should instead make a third table to connect the two that just has the FKs for each. Example is Students table and Classes table should have a Students_Classes table that has a row that has 2 FKs, one to Students table and one to the Classes table. 

`ER Diagram` is the box diagram that I like. Used more for the database side of things (defines tables and their relationships).

`UML Diagram` is used more commonly as a class diagram for software side of things (defines classes and their attributes and functions).

### ODS (Operational Data Store)

Whatever an application uses to store its data, often changes constantly. Any data that impacts their day to day operations. For example, the DB that Amazon uses that stores every order that gets executed and the info related to it. Different from a data warehouse, which changes every night for instance. ODS is row oriented and can do lots of transactions in a second and can support lots of web servers that are hammering it. Oracle, Microsoft SQL Server, PostgreSQL, MySQL (all of these are OLTP Online Transaction Processing). Best for day to day data high transaction volume (like running an app, website, or a game).

### Aurora

A MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. So this is an ODS. Competes with Oracle. Can have massive clusters (Doordash has a single cluster for 10TB and billions of rows, The Pokemon Company handles 300 logins per second, Dow Jones migrated from on-premise to Aurora with no disruption to service). ROW ORIENTED.

### Redshift

Makes it simple and cost effective to run high performance queries on petabytes of semi-structured and structured data so that you can build powerful reports and dashboards using QuickSight or other business intelligence tools. Intuit uses Redshift for business intelligence. Used for querying large data sets quickly. (OLAP Online Analytics Processing). Better for analytics. Very expensive, great for massive processing jobs (can do huge parallel processing because has lots of available CPUs). COLUMN ORIENTED (COLUMNAR).

### Spectrum

Serverless. Queries S3. More control over performance because it uses the redshift cluster size. Uses virtual table from glue catalog when querying S3. Use this for queries closely tied to a Redshift DW, can also be used to join data between S3 and Redshift and load the results into Redshift. Cheaper than Redshift because storage in S3 is cheaper and has an ephemeral compute. There is overhead cost, but that can be recouped if you do a giant query and fire up lots of EC2s for a short period of time. Can read data from S3 and transform it and then load it into Redshift. Can also be used for some ad hoc needs.

### Athena

Serverless. Queries S3. Uses pooled resources provided by AWS, so less control over performance than Spectrum. Uses virtual table from glue catalog when querying S3. Use if all your data is in S3 and you do not want to analyze Redshift data.

### Data Warehouse

`Data Warehouse`: Repository for structured, filtered data that has already been processed for a specific purpose. Use a very particular schema. Used for SQL DBs. Often used by analysts. More secure. Less flexible. 

`Data Mart`: A structure/access pattern specific to DW environments, used to retrieve client-facing data. The data mart is a subset of the data warehouse and is usually oriented to a specific business line or team.

### Data Lake

`Data Lake`: Vast pool of raw data, purpose of which is not defined. Usually relates to a particular part of the business. Schemaless. Similar to non-relational NoSQL DBs. Often used by data scientists (usually requires more knowledge to use than a DW). Less secure. More flexible. In general, data lakes are good for analyzing data from different, diverse sources from which initial data cleansing can be problematic. Good for IoT and ML.

`Data Ocean`: Like a data lake but applies to the entire scope of the business.

`Data Reservoir`: Partly filtered part of the data lake that has been made ready for consumption.

### Data Lakehouse

A data lakehouse is a new, open data management architecture that combines the flexibility, cost-efficiency, and scale of data lakes with the data management and ACID transactions of data warehouses, enabling business intelligence (BI) and machine learning (ML) on all data.

### ACID

`Atomicity`: transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single unit, which either succeeds completely or fails completely, meaning if any of the statements in a transaction fail, the entire transaction fails and the db is left unchanged. Must guarantee atomicity in each situation including power failures, errors, and crashes. Prevents updates from occurring only partially.

`Consistency`: ensures that a transaction can only bring the db from one valid state to another, maintaining db invariants. Any data written must be valid according to all defined rules, including constraints, cascades, and triggers.

`Isolation`: transactions are often executed concurrently. Isolation ensures that concurrent execution of transactions leaves the db in the same state that would have been obtained if the transactions were executed sequentially.

`Durability`: once a transaction is committed, it will remain committed even in a system failure. Usually means completed transactions or effects are recorded in non-volatile memory.

### Data Modeling

Data modeling is the method of documenting complex software design as a diagram so that anyone can easily understand. It is a conceptual representation of data objects that are associated between various data objects and the rules.

### ETL (Extract, Transform, Load)

The process data engineers use to extract data from different sources, transform the data into a usable and trusted resource, and load that data into the systems end-users can access and use downstream to solve business problems.

Extract

The first step of this process is extracting data from the target sources that are usually heterogeneous such as business systems, APIs, sensor data, marketing tools, and transaction databases, and others. As you can see, some of these data types are likely to be the structured outputs of widely used systems, while others are semi-structured JSON server logs. There are different ways to perform the extraction: Three Data Extraction methods:
- Partial Extraction – The easiest way to obtain the data is if the if the source system notifies you when a record has been changed
- Partial Extraction (with update notification) - Not all systems can provide a notification in case an update has taken place; however, they can point to those records that have been changed and provide an extract of such records.
- Full extract – There are certain systems that cannot identify which data has been changed at all. In this case, a full extract is the only possibility to extract the data out of the system. This method requires having a copy of the last extract in the same format so you can identify the changes that have been made.

Transform

The second step consists of transforming the raw data that has been extracted from the sources into a format that can be used by different applications. In this stage, data gets cleansed, mapped and transformed, often to a specific schema, so it meets operational needs. This process entails several types of transformation that ensure the quality and integrity of data. Data is not usually loaded directly into the target data source, but instead it is common to have it uploaded into a staging database. This step ensures a quick roll back in case something does not go as planned. During this stage, you have the possibility to generate audit reports for regulatory compliance, or diagnose and repair any data issues.

Load

Finally, the load function is the process of writing converted data from a staging area to a target database, which may or may not have previously existed. Depending on the requirements of the application, this process may be either quite simple or intricate. Each of these steps can be done with ETL tools or custom code.

What is an ETL pipeline?

An ETL pipeline (or data pipeline) is the mechanism by which ETL processes occur. Data pipelines are a set of tools and activities for moving data from one system with its method of data storage and processing to another system in which it can be stored and managed differently. Moreover, pipelines allow for automatically getting information from many disparate sources, then transforming and consolidating it in one high-performing data storage.

Challenges with ETL

While ETL is essential, with this exponential increase in data sources and types, building and maintaining reliable data pipelines has become one of the more challenging parts of data engineering. From the start, building pipelines that ensure data reliability is slow and difficult. Data pipelines are built with complex code and limited reusability. A pipeline built in one environment cannot be used in another, even if the underlying code is very similar, meaning data engineers are often the bottleneck and tasked with reinventing the wheel every time. Beyond pipeline development, managing data quality in increasingly complex pipeline architectures is difficult. Bad data is often allowed to flow through a pipeline undetected, devaluing the entire data set. To maintain quality and ensure reliable insights, data engineers are required to write extensive custom code to implement quality checks and validation at every step of the pipeline. Finally, as pipelines grow in scale and complexity, companies face increased operational load managing them which makes data reliability incredibly difficult to maintain. Data processing infrastructure has to be set up, scaled, restarted, patched, and updated - which translates to increased time and cost. Pipeline failures are difficult to identify and even more difficult to solve - due to lack of visibility and tooling. Regardless of all of these challenges, reliable ETL is an absolutely critical process for any business that hopes to be insights-driven. Without ETL tools that maintain a standard of data reliability, teams across the business are required to blindly make decisions without reliable metrics or reports. To continue to scale, data engineers need tools to streamline and democratize ETL, making the ETL lifecycle easier, and enabling data teams to build and leverage their own data pipelines in order to get to insights faster.

### ETL vs ELT

ELT is better for data lakes because you want to store the raw data, can also go back and do transformations in different ways (might not know the transformations in advance, so just load it first before transforming it). Can also move data more quickly doing ELT. Can also load it and then transform it 2 different ways instead of doing one before loading it.

### Data Streaming

Streaming analytics, also known as event stream processing, is the analysis of huge pools of current and “in-motion” data through the use of continuous queries, called event streams. These streams are triggered by a specific event that happens as a direct result of an action or set of actions, like a financial transaction, equipment failure, a social post or a website click or some other measurable activity. The data can originate from the Internet of Things (IoT), transactions, cloud applications, web interactions, mobile devices, and machine sensors. By using streaming analytics platforms organizations can extract business value from data in motion just like traditional analytics tools would allow them to do with data at rest. Real-time streaming analytics help a range of industries by spotting opportunities and risks.
 
#### Streaming Analytics

The Advantages of Streaming Analytics

- Data visualization. Keeping an eye on the most important company information can help organizations manage their key performance indicators (KPIs) on a daily basis. Streaming data can be monitored in real time allowing companies to know what is occurring at every single moment
- Business insights. In case an out of the ordinary business event occurs, it will first show up in the relevant dashboard. It can be used in cybersecurity, to automate detection and response to the threat itself. This is an area where abnormal behavior should be flagged for investigation right away.
- Increased competitiveness. Businesses looking to gain a competitive advantage can use streaming data to discern trends and set benchmarks faster. This way they can outpace their competitors who are still using the sluggish process of batch analysis.
- Cutting preventable losses. With the help of streaming analytics, we can prevent or at least reduce the damage of incidents like security breaches, manufacturing issues, customer churn, stock exchange meltdowns, and social media crisis.
- Analyzing routine business operations. Streaming analytics offers organizations an opportunity to ingest and obtain an instant insight from the real-time data that is pouring in.
- Finding missed opportunities. The streaming and analyzing of Big Data can help companies to uncover hidden patterns, correlations and other insights. Companies can get answers from it almost immediately being able to upsell, and cross-sell clients based on what the information presents.
- Create new opportunities. The existence of streaming data technology brings the type of predictability that cuts costs, solves problems and grows sales. It has led to the invention of new business models, product innovations, and revenue streams.
- Your company can now monitor in real time: manufacturing closed-loop control systems; the health of a network or a system; field assets such as trucks, oil rigs, vending machines; and financial transactions such as authentications and validations.
- Your company will be able to answer questions like:
    - How many customers do you have in your store at this very moment, and what are they most likely to purchase?
    - Which vehicles in our fleet are using the most fuel and why?
    - Is there a machinery in your factory that could fail in the next five business days, and what spare parts will be required to keep it running?

### Data Normalization

Repeating for order data city info may be best in order table instead of creating an address table. You need to determine what level of normalization you want. Normalization is the technique to order data into tables to reduce redundancy. Data normalization can slow down updates because there are more tables to update, also creates longer task because there are more tables to join.

### Orchestration

The goal of orchestration is to streamline and optimize the execution of frequent, repeatable processes and thus to help data teams more easily manage complex tasks and workflows. Anytime a process is repeatable, and its tasks can be automated, orchestration can be used to save time, increase efficiency, and eliminate redundancies.

What is the difference between process orchestration and process automation?

While automation and orchestration are highly complementary, they mean different things. Automation is programming a task to be executed without the need for human intervention. Orchestration is the configuration of multiple tasks (some may be automated) into one complete end-to-end process or job. Orchestration software also needs to react to events or activities throughout the process and make decisions based on outputs from one automated task to determine and coordinate the next tasks.

### The Difference Between Data and Big Data Analytics

Prior to the invention of Hadoop, the technologies underpinning modern storage and compute systems were relatively basic, limiting companies mostly to the analysis of "small data." Even this relatively basic form of analytics could be difficult, though, especially the integration of new data sources. With traditional data analytics, which relies on the use of relational databases (like SQL databases), made up of tables of structured data, every byte of raw data needs to be formatted in a specific way before it can be ingested into the database for analysis. This often lengthy process, commonly known as extract, transform, load (or ETL) is required for each new data source. The main problem with this 3-part process and approach is that it’s incredibly time and labor intensive. 

Once data was inside the database, though, in most cases it was easy enough for data analysts to query and analyze. But then along came the Internet, eCommerce, social media, mobile devices, marketing automation, Internet of Things (IoT) devices, etc., and the size, volume, and complexity of raw data became too much for all but a handful of institutions to analyze in the normal course of business.

Big data analytics is the often complex process of examining large and varied data sets - or big data - that has been generated by various sources such as eCommerce, mobile devices, social media and the Internet of Things (IoT). It involves integrating different data sources, transforming unstructured data into structured data, and generating insights from the data using specialized tools and techniques that spread out data processing over an entire network. The amount of digital data that exists is growing at a fast pace, doubling every two years. Big data analytics is the solution that came with a different approach for managing and analyzing all of these data sources. While the principles of traditional data analytics generally still apply, the scale and complexity of big data analytics required the development of new ways to store and process the petabytes of structured and unstructured data involved. The demand for faster speeds and greater storage capacities created a technological vacuum that was soon filled by new storage methods, such as data warehouses and data lakes, and nonrelational databases like NoSQL, as well as data processing and data management technologies and frameworks, such as open source Apache Hadoop, Spark, and Hive. Big data analytics takes advantage of advanced analytic techniques to analyze really big data sets that include structured, semi-structured and unstructured data, from various sources, and in different sizes from terabytes to zettabytes.

The Most Common Data Types Involved in Big Data Analytics Include: Web, Text, Time and location, Real-time media, Smart grid and sensor, Social network, Linked, and Network.

Big data analytics helps organizations harness their data and use advanced data science techniques and methods, such as natural language processing, deep learning, and machine learning, uncovering hidden patterns, unknown correlations, market trends and customer preferences, to identify new opportunities and make more informed business decisions.

Advantages of Using Big Data Analytics Include: Cost reduction, Improved decision making, New products and services, Fraud detection.

### Apache Hadoop

High Availability Distributed Object Oriented Platform (HADOOP). Does Map Reduce.  High availability via parallel distribution of object-oriented tasks. Apache Hadoop is an open source, Java-based software platform that manages data processing and storage for big data applications. The platform works by distributing Hadoop big data and analytics jobs across nodes in a computing cluster, breaking them down into smaller workloads that can be run in parallel. Hadoop isn’t a solution for data storage or relational databases. Instead, its purpose as an open-source framework is to process large amounts of data simultaneously in real-time.

### Apache Spark

Is meant to solve the problem created by map reduce. Map reduce takes a computation on petabytes of data and breaks it up by parallelizing it and then stitching the small answers back together to get an answer to the big computation that was too big to execute. The problem is map reduce is hard to code (very tedious, writing a lot of the same things over again), so spark (written in scala), is a library that makes it easier to do the map reduce operation. PySpark is just Spark in python and is very similar to Pandas.

### Hadoop vs Spark

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

### Apache Hive

Apache Hive was the early go-to solution for how to query SQL with Hadoop. This module emulates the behavior, syntax and interface of MySQL for programming simplicity. It’s a great option if you already heavily use Java applications as it comes with a built-in Java API and JDBC drivers. Hive offers a quick and straightforward solution for developers but it’s also quite limited as the software’s rather slow and suffers from read-only capabilities.

### Apache Kafka

Apache Kafka is a distributed data store optimized for ingesting and processing streaming data in real-time. Streaming data is data that is continuously generated by thousands of data sources, which typically send the data records in simultaneously. A streaming platform needs to handle this constant influx of data, and process the data sequentially and incrementally.

Kafka provides three main functions to its users:

Publish and subscribe to streams of records
Effectively store streams of records in the order in which records were generated
Process streams of records in real time
Kafka is primarily used to build real-time streaming data pipelines and applications that adapt to the data streams. It combines messaging, storage, and stream processing to allow storage and analysis of both historical and real-time data.  

Why would you use Kafka?
Kafka is used to build real-time streaming data pipelines and real-time streaming applications. A data pipeline reliably processes and moves data from one system to another, and a streaming application is an application that consumes streams of data. For example, if you want to create a data pipeline that takes in user activity data to track how people use your website in real-time, Kafka would be used to ingest and store streaming data while serving reads for the applications powering the data pipeline. Kafka is also often used as a message broker solution, which is a platform that processes and mediates communication between two applications.

How does Kafka work?
Kafka combines two messaging models, queuing and publish-subscribe, to provide the key benefits of each to consumers. Queuing allows for data processing to be distributed across many consumer instances, making it highly scalable. However, traditional queues aren’t multi-subscriber. The publish-subscribe approach is multi-subscriber, but because every message goes to every subscriber it cannot be used to distribute work across multiple worker processes. Kafka uses a partitioned log model to stitch together these two solutions. A log is an ordered sequence of records, and these logs are broken up into segments, or partitions, that correspond to different subscribers. This means that there can be multiple subscribers to the same topic and each is assigned a partition to allow for higher scalability. Finally, Kafka’s model provides replayability, which allows multiple independent applications reading from data streams to work independently at their own rate.

Queuing

Publish-Subscribe

Benefits of Kafka's approach
Scalable
Kafka’s partitioned log model allows data to be distributed across multiple servers, making it scalable beyond what would fit on a single server. 

Fast
Kafka decouples data streams so there is very low latency, making it extremely fast. 

Durable
Partitions are distributed and replicated across many servers, and the data is all written to disk. This helps protect against server failure, making the data very fault-tolerant and durable. 

Dive deep into Kafka's architecture
Kafka remedies the two different models by publishing records to different topics. Each topic has a partitioned log, which is a structured commit log that keeps track of all records in order and appends new ones in real time. These partitions are distributed and replicated across multiple servers, allowing for high scalability, fault-tolerance, and parallelism. Each consumer is assigned a partition in the topic, which allows for multi-subscribers while maintaining the order of the data. By combining these messaging models, Kafka offers the benefits of both. Kafka also acts as a very scalable and fault-tolerant storage system by writing and replicating all data to disk. By default, Kafka keeps data stored on disk until it runs out of space, but the user can also set a retention limit. Kafka has four APIs:

Producer API: used to publish a stream of records to a Kafka topic.
Consumer API: used to subscribe to topics and process their streams of records.
Streams API: enables applications to behave as stream processors, which take in an input stream from topic(s) and transform it to an output stream which goes into different output topic(s).
Connector API: allows users to seamlessly automate the addition of another application or data system to their current Kafka topics.

### Apache Parquet

Apache Parquet is an open source, column-oriented data file format designed for efficient data storage and retrieval. It provides efficient data compression and encoding schemes with enhanced performance to handle complex data in bulk. Apache Parquet is designed to be a common interchange format for both batch and interactive workloads. It is similar to other columnar-storage file formats available in Hadoop, namely RCFile and ORC.

Characteristics of Parquet

- Free and open source file format.
- Language agnostic.
- Column-based format - files are organized by column, rather than by row, which saves storage space and speeds up analytics queries.
- Used for analytics (OLAP) use cases, typically in conjunction with traditional OLTP databases.
- Highly efficient data compression and decompression.
- Supports complex data types and advanced nested data structures.

Benefits of Parquet

- Good for storing big data of any kind (structured data tables, images, videos, documents).
- Saves on cloud storage space by using highly efficient column-wise compression, and flexible encoding schemes for columns with different data types.
- Increased data throughput and performance using techniques like data skipping, whereby queries that fetch specific column values need not read the entire row of data.
- Apache Parquet is implemented using the record-shredding and assembly algorithm, which accommodates the complex data structures that can be used to store the data. Parquet is optimized to work with complex data in bulk and features different ways for efficient data compression and encoding types. This approach is best especially for those queries that need to read certain columns from a large table. Parquet can only read the needed columns therefore greatly minimizing the IO.

Advantages of Storing Data in a Columnar Format:

- Columnar storage like Apache Parquet is designed to bring efficiency compared to row-based files like CSV. When querying, columnar storage you can skip over the non-relevant data very quickly. As a result, aggregation queries are less time-consuming compared to row-oriented databases. This way of storage has translated into hardware savings and minimized latency for accessing data.
- Apache Parquet is built from the ground up. Hence it is able to support advanced nested data structures. The layout of Parquet data files is optimized for queries that process large volumes of data, in the gigabyte range for each individual file.
- Parquet is built to support flexible compression options and efficient encoding schemes. As the data type for each column is quite similar, the compression of each column is straightforward (which makes queries even faster). Data can be compressed by using one of the several codecs available; as a result, different data files can be compressed differently.
- Apache Parquet works best with interactive and serverless technologies like AWS Athena, Amazon Redshift Spectrum, Google BigQuery and Google Dataproc.

Difference Between Parquet and CSV

CSV is a simple and common format that is used by many tools such as Excel, Google Sheets, and numerous others. Even though the CSV files are the default format for data processing pipelines it has some disadvantages:

- Amazon Athena and Spectrum will charge based on the amount of data scanned per query.
- Google and Amazon will charge you according to the amount of data stored on GS/S3.
- Google Dataproc charges are time-based.

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improved scan and deserialization time, hence the overall costs. The following table compares the savings as well as the speedup obtained by converting data into Parquet from CSV.

Dataset | Size on Amazon S3 | Query Run Time | Data Scanned | Cost
--- | --- | --- | --- | ---
Data stored as CSV files | 1 TB | 236 seconds | 1.15 TB | $5.75
Data stored in Apache Parquet Format | 130 GB | 6.78 seconds | 2.51 GB | $0.01
Savings | 87% less when using Parquet | 34x faster | 99% less data scanned | 99.7% savings

### Snowflake Schema

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

### DBT

DBT is within warehouse airflow, benefit is that you can get the result using sql. Builds based off of how you write sql files, self resolves what happens up and downstream, gives out of the box testing. Lets you write macros. Bridges gap between data analysts and engineers. Reduces barrier to entry to work with data pipelines.

### Databricks

Apache tool used to work with Spark. Can use iPython Notebooks. All data, analytics, and AI in one platform. Multicloud and open source.
