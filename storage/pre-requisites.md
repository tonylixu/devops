## Storage Basics
* Concurrency: Do you understand threads, deadlock and starvation? What happens when multiple processes/threads are trying to modify the same data? A basic understanding of read and write locks.
* Newworking: Do you roughly understand basic networking protocls like TCP and UDP?
* File systems: You should understand the systems you are building upon. Do you know roughly how an OS, file system, and database work? Do you know about the various levels of caching in a modern OS?

## Basic terminologies
* Replication: Replication refers to frequently copying the data across multiple machines. Post replication, multiple copies of data exists across machines. 
* Consistency: Assuming you have a storage system which has more than more machine, consistency implies that the data is same across the cluster, so you can read or write to/from any node and get the same data. Eventual consistency: Exactly what the name suggests. In a cluster, if multiple machines store the same data, an eventual consistent model implies that all machines will have the same data eventually. Its possible that at a given instance, those machines have different versions of the same data (temporarily inconsistent) but they will eventually reach a state where they have the same data.
* Availability: In a context of database cluster, availability refers to the ability to always respond to the queries (read or write) irrespective of nodes going down.
* Partition Tolerance: In the context of a database cluster, cluster continues to function even if there is a "partition" (communications break) between two nodes.
* Vertical scaling and Horizontal scaling : In simple terms, to scale horizontally is adding more servers. To scale vertically is to increase the resources of the server ( RAM, CPU, storage, etc. ). 

## CAP Theorem 
CAP states that in a distributed system, it is impossible to simultaneously guarantee all of the following:
* Consistency
* Availability
* Partition Tolerance