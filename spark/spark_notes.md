# Spark and PySpark Guide

## Purpose of Spark
Pandas is great... until we have too much data.
If we have too much data for a single machine, we need to parallelize it using Spark.
To do this we use RDDs.

Big data simply means data that would not fit in a single machine's storage,
let alone RAM.

## RDD
RDD stands for Resilient (it is in memory), Distributed (on multiple machines) Dataset
This is what Spark lets us use to parallelize the data as we load something too big
to handle on a single machine.

Immutable distributed collection of data, which is not tabular like Spark dataframes.
Has no data schema, which means it has no defined data types.
Dataframes allows for more API options and better under the hood optimization.

## Differences between Apache Spark and PySpark
Spark is the most powerful big data tool, which is a parallel distributed processing framework. The core power of Spark is to handle huge amounts of data.
Spark supports: Scala, Java, Python, and R
PySpark is an interface for Spark in python.

## Features of PySpark
It can distribute data across nodes and parallelize tasks
Immutable: you can create a new dataframe by applying transformations on the existing dataframe
Lazy evaluation: it uses DAG for computation
Cache & Persistence: data can be cached to memory/disk depending on the situation
Fault Tolerance: it can recover data if it is lost
Supports SQL
Supports several modes of deploymen: Standalone, Apache Mesos, Hadoop YARN, K8S. These are all different cluster managers
Read data from PostgreSQL, Cassandra, S3, HDFS, Blob, etc. It supports many other data sources.
PySpark lets you use python to run transformations on RDDs and to write Spark code, but it is a little slower (will be easier for me though given my Python/Pandas knowledge)

## Parts pf PySpark

- Spark SQL + DataFrames
- Streaming
- MLlib (Machine learning)
- GraphX (Graph computation)

## Architecture

You need to initiate a Spark session to send commands and receive output from a cluster. This object is the tool for interacting with Spark.
A session communicates with the SparkContext, which is the master node in the cluster. It assigns each of the nodes in the cluster tasks and coordinates them.
Each node that performs tasks for the master node is called a worker node.
The cluster manager is responsible for distributing the cluster's resources.
In each worker node is an executor, which executes tasks, and has a cache.

## Setting Up

from pyspark.sql import SparkSession

if you need to install, do:
pip install pyspark

spark = SparkSession.builder.appName('test').getOrCreate()

## Loading data

This will load all data into strings:
df = spark.read.option('header','true').csv('/usr/data/location/filename.csv')

This will load all data based on the data type for each column:
schema = 'Age INTEGER, Gender STRING, FirstName STRING'
df = spark.read.csv('/usr/data/location/filename.csv', schema=schema, header=True)

You can also pass arguments like:
nullValue='NA'
inferSchema=True

## Saving Data

This will let you save to a new file, but won't let you overwrite an existing file:
df.write.format("csv").save("location/to/save/filename.csv")

To overwrite a file, do:
df.write.format("csv").mode("overwrite").save("location/to/save/filename.csv")

## Useful Queries and Functions

Count number of rows in DF
df.count()

Show first 3 rows of table
df.show(3)

Show first 3 rows of Age column
df.select("Age").show(3)

Show first 3 rows of Age and Gender columns
df.select(["Age", "Gender"]).show(3)

## Pandas vs PySpark DFs

Both represent data with rows, columns, and schema.
PySpark DFs support distributed computation, but Pandas does not.
If you know Pandas, then moving to PySpark will be natural

## DAGs

This is the way Spark runs computations and transformations. It builds a graph
and does Lazy execution and only does things when it must, which provides better performance by optimization by planning ahead

As you transform an object, a new DF is created, you do not write over the previous one because they are immutable.

### PySpark Commands

#### Transformations

Added to the DAG, but does not get to actually be executed until an action is called. Only transforms one DF into another, does not change the input DF.

#### Actions

Make PySpark execute the DAG, but does not create a new DF, instead they output the result of the DAG to you, the user.

### Caching

Every time you run a DAG, it will be recomputed from the beginning. The results are not saved in memory, but if you want to save the result, you can use the Cache by doing:
df.cache() 
This will save it on the machine's cache memory (be careful with sizes here!). By default, the cached DF is stored to RAM and is unserialized. You can choose to save to disk, or serialize it, or both instead.

## Collecting

This will take all the data from the worker nodes and try to collect it on the master node (be very careful with this, because this file will have to fit in the master node's memory!). You will rarely use this command explicitly.
df.collect()

## Converting PySpark DF to Pandas DF

pd_df = df.toPandas()

## Converting Pandas DF to PySpark DF

spark_df = spark.createDataFrame(pd_df)

## Column Data Types

To show column data types and see if they accept Null values, do:
df.printSchema()

you can also do:
df.dtypes()

## Change Column Data Type

from pyspark.sql.types import FloatType
df = df.withColumn("Age", df.Age.cast(FloatType()))

## Remove Column

df.drop('ColumnName')

## Renaming Columns


