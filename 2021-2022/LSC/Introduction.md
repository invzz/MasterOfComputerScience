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
  
