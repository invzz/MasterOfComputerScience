# Large Scale Computing

An introductury lecture 

---

## The Big Data era

We are living a big data era and computations are becoming data centric. This requies some specialized software architecture and sometimes specialized hardware architecture.

- We have to deal with big amount of data!
- "Large Scale" generally refers to the use of multiple nodes that collaborate on a few levels to complete a given computation
- the nodes can use middleware of some kind, allowing multiple nodes to share the load of processing incoming requests in software
- the nodes could be collaborating at the operating system level or running to a cluster
- data intensive computation.

## Compute intensive Vs Data intensive

- compute intensive app
-
- s devote most of their exection time do do some sort of computation.
  - High Performance Computing
  
- data intensive apps spend most of the time to I/O and data manipulation.
  - ADM, Data Werehousing, IoT

## Data-intensive / centric computing

A class of parallel computing applications which use a data parallel approach to process large volumes of data, typically terabytes of data in size.

it is a way to design an application to simplify life of developers and final users.

in very simple terms you want to avoid copying data, which could be petabytes of data.

## Big Data?

- 40 Zettabytes of data 2020
- IoT will largerly contribute to increase Big Data challenges
- Big Data requires new computing approaches (scale change everything)

## The three (Main)Vs

We have to make some compromise!

- **Volume**
  - terabytes
  - records
  - transactions
  - tables, files
- **Velocity**
  - batch
  - near time
  - real time
  - streams
- **Variety**
  - unstructured
  - semistructred
  - structured
  
Other Vs are important too:

- **Value**
- **Variability**
- **Veracity**
- **Visualization**

## How to deal with Big Data?

- Batch processing
  - Ex. MapReduce
- data stream processing

## Parallel programming

Break processing into parts that can be executed concurrently on multiple processors. The challenge is to identify tasks that can run concurrently in groups of data: Not all problem can be parallelized!

*can be a difficul task!*

- how do we assign tasks to workers?
- what if we have more tasks than slots?
- what happens when a task fails?
- how do we handle distribuited synchronization?
  
**Dealing with Big data storage is not trivial!** Data volumes are massive, reliably storing PBs of data is a challenge, Disk/hw/network failures.

## Typical Big Data Problem

- iterate over a large number of records
- extract something of interest from each record
- shuffle and sort intermediate results
- aggregate intermediate results
- generate final output

In general there is a **Map-reduce** approach if you tackle your problem this way.

- Map phase analyze locally the data.
- Reduce applies a kind of compression before "copying data" into the output stream.

So map reduce is an Divide et conquer methodology to tackle data centric applications.

- Partition a large problem
- Compute indimpendent sub-problems in parallel
- Combine intermediate results

---

## High level Architecture

When programming distribuited systems always keep in mind the underlying architecture.

---

The nice feature of Map-Reduce is taht is a very general paradigm that can be used to solve a wide range of problems.

## Relation to functional programming

- functional programming have in-build map and reduce functions
  - ex caml, python, js, ts, F#, C#

## Data-intensive computing as a Service

Moving among abstraction levels from low to high we have

- bare metal
- resource manager
  - k8s, docker ...
- distribuited storage
  - BigTabe, Amazon S3 ...
- Operational stores (sql, spinner, dynamo, cassandra), messagge bus(kafka...), meatada (aws catalog)
- Cache, other services, analytics engines, map
- Analytics UI
  - tableau
  - fblearner

## Kafka

is a distribuited application for collecting data, filter data, aggregate data

## Spark 

Map-reduce distributed processing application 

## LOOK at!

- Amazon spark
- Google cloud Platform
- DataProc
- Leonardo Labs da vinci 1
- Engineering dive platform
- liguria dicitale
- flairbit senseioty platform

