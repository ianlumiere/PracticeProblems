# Spark and PySpark Guide

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
PySpark lets you use python to write Spark code, but it is a little slower (will be easier for me though given my Python/Pandas knowledge)

