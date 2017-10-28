## Steps to Approach a Probelm

### Feature expectations:
It is extremely important to get a very clear understanding of whats the requirement for the question.

### Estimation
Estimate the scale required for the system. The goal of this step is to understand the level of sharding required (if any) and to zero down on the design goals for the system.
Examples: If the total data required for the system fits on a single machine, we might not need to go into sharding and the complications that go with a distributed system design. OR if the most frequently used data fits on a single machine, in which case caching could be done on a single machine.

### Design Goals
Figure out what are the most important goals for the system. It is possible that there are systems which are latency systems in which case a solution that does not account for it, might lead to a bad design. Or a system needs high availability that we can sacrefies the consistency.

### Skeleton of The Design
As such, a good strategy is to discuss a very high level with the interviewer and go into a deep dive of components as enquired by the interviewer.

### Deep Dive

### Useful reads
* Master Slave : https://www.quora.com/What-are-Master-and-Slave-databases-and-how-does-pairing-them-make-web-apps-faster

* Real life example of scaling using MySQL :https://engineering.pinterest.com/blog/sharding-pinterest-how-we-scaled-our-mysql-fleet/

* https://en.wikipedia.org/wiki/Paxos_(computer_science)