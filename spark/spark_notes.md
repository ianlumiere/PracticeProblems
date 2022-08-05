# Spark and PySpark Guide

## Purpose of Spark
Pandas is great... until we have too much data.
If we have too much data for a single machine, we need to parallelize it using Spark.
To do this we use RDDs.

## RDD
RDD stands for Resilient (it is in memory), Distributed (on multiple machines) Dataset
This is what Spark lets us use to parallelize the data as we load something too big
to handle on a single machine.

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

