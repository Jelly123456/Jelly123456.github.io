title: Apache spark
date: 21-April-2021
author: YiLi

# Source

[Source](https://www.udemy.com/course/scala-and-spark-2-getting-started/learn/lecture/9656744?LSNPUBID=JVFxdTr9V80&components=purchase%2Ccacheable_buy_button%2Cbuy_button%2Crecommendation&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-NEYgc584Fxj.ju4fAiJ35A&utm_medium=udemyads&utm_source=aff-campaign#overview)

[Apache spark VS Hadoop](https://www.scnsoft.com/blog/spark-vs-hadoop-mapreduce)

# Apache spark

* A shiny new big data platform
* A open source project by Apache Software Foundation

# Apache spark VS Hadoop

* Key difference
  * Spark can do in memory
  * Hadoop mapReduce has to read from and write to a disk
* the speed of processing differs significantly
  * Apache Spark is potentially 100 times faster than Hadoop MapReduce
* the volume of data processed also differs
  * Hadoop MapReduce is able to work with far larger data sets than Spark
* Apache Spark utilizes RAM and isn't tied to Hadoop's two-stage paradigm
* Apache Spark works well for smaller data sets that can all fit into a server's RAM
* Hadoop is more cost effective processing massive data sets
* Apache Spark is now more popular that Hadoop MapReduce

## Tasks Hadoop MapReduce is good for:

* Linear processing of huge data sets.
  * Hadoop MapReduce allows parallel processing of huge amounts of data. It breaks a large chunk into smaller ones to be processed separately on different data nodes and automatically gathers the results across the multiple nodes to return a single result. In case the resulting dataset is larger than available RAM, Hadoop MapReduce may outperform Spark.
* Economical solution, if no immediate results are expected.
  * MapReduce is a good solution if the speed of processing is not critical. For instance, if data processing can be done during night hours, it makes sense to consider using Hadoop MapReduce.

## Tasks Spark is good for:

* Fast data processing.
  * In-memory processing makes Spark faster than Hadoop MapReduce – up to 100 times for data in RAM and up to 10 times for data in storage.
* Iterative processing.
  * If the task is to process data again and again – Spark defeats Hadoop MapReduce. Spark’s Resilient Distributed Datasets (RDDs) enable multiple map operations in memory, while Hadoop MapReduce has to write interim results to a disk.
* Near real-time processing.
  * If a business needs immediate insights, then they should opt for Spark and its in-memory processing.
* Graph processing.
  * Spark's computational model is good for iterative computations that are typical in graph processing. And Apache Spark has GraphX – an API for graph computation.
* Machine learning
  * Spark has MLlib – a built-in machine learning library, while Hadoop needs a third-party to provide it. MLlib has out-of-the-box algorithms that also run in memory.
* Joining datasets
  * Due to its speed, Spark can create all combinations faster, though Hadoop may be better if joining of very large data sets that requires a lot of shuffling and sorting is needed.

# Architecture of Spark(Updating)

# Resilient Distributed Datasets(RDD)

* Dataset
* Distributed
* Resilient
  * Recover from failure
