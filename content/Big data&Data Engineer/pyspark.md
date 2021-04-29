title: pyspark - A python API for spark
date: 21-April-2021
author: YiLi

[Source](https://medium.com/javarevisited/5-free-courses-to-learn-apache-spark-in-2020-bdff2d60c800)

# Steps to set up the environment in Windows

## 1. Setup Python

* Commands to check python is installed on Windows

  * open a command prompt
  * `python`

## 2. Install PyCharm

* Install PyCharm

## 3. Install Spark

* Install JDK
* Dowanload spark

  * [Dowanload Link](https://spark.apache.org/downloads.html)
* Setup Spark

  * set "SPARK_HOME" environment variable to the location where the "spark" is installed
  * add "%SPARK_HOME%\bin" to "path" variable
  * open a terminal and type "pyspark".
* Install "winutils.exe" to aviod exception error

  * download "winutils.exe"
  * save it to a folder where "spark" is installed (SPARK_HOME\bin)
  * set "HADOOP_HOME" to the location where "spark" is installed
  * add "%HADOOP_HOME%\bin" to "path" variable
* Add SPARK to pycharm IDE

  * open "File" => "Settings.." => Project:xxx => Project structure => "Add Content Root"
    * SPARK folder \python
    * SPARK folder \python\py4j-0.10.9-src.zip

## 4. Start developing spark applications with pycharm
