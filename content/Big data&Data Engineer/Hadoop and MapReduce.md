title: Hadoop and MapReduce
date: 19-April-2021
author: YiLi

[Good blog from internet](https://medium.com/swlh/5-free-online-courses-to-learn-big-data-hadoop-and-spark-in-2019-a553e6ccfe30)

[Source 1](https://www.udemy.com/course/hadoopstarterkit/learn/lecture/2995948#overview)

[Source 2](https://hadoop.apache.org/)

# What is big data

* Big volume
* High velocity
* Variety

# Problems with big data

With traditional platform, a ETF task would take a very long time for big data because of low the data access rate and long program computation time.

# Hadoop

* A big data platform
* A open source project by Apache Software Foundation

# HDFS - Hadoop Distributed File System

* If you upload a file into HDFS, it will automatically split into blocks with a fixed size of 128MB
* HDFS responsibilities
  * takes care of placing the blocks in differnet nodes
  * takes care of replicating each block to be more than one node, by feault, it will replicates to be 3 nodes
* Benefits of HDFS
  * Support distributed processing
    * Blocks
  * Handle failure
    * Replicate blocks
  * Scalability
    * Able to support future expansion
  * Cost effective
    * Commodity hardware

# MapReduce

* Description
  * MapReduce is a programming model for distributed computing
  * It is not a programming language, but a model
  * It can process huge datasets in a distributed fashion
* Phases
  * Map phase
    * Assign each individual mapper
  * Shuffle phase
  * Reduce phase
    * Aggregrate the results from map phase

# Apache Pig

* Description
  * Developed in Yahoo
  * To make mapreduce accessible to anyone who want to use hadoop clusters
  * The lines of codes will be less than that is written in Java

# Apache Hive

* Description
  * Developed by Facebook
  * Widely used in industry
  * Able to create table structures for your data set and write SQL quries to analyze.
* Pig VS Hive
  * These two similar tools can be used in the same hadoop project
  * Pig is suitable to run standard nightly ETL jobs, like extracting data, transforming data and doing some pre-defined calculations
  * Hive can be used by developers, data analytics, data scientists on a daily ad-hoc data analysis
  *
