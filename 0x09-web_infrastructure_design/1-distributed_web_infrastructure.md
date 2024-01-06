
Description:

This distributed web infrastructure aims to alleviate traffic on the primary server by leveraging a replica server, supported by a load balancer responsible for efficiently distributing the workload between the primary and replica servers.

Specifics About This Infrastructure:

Load Balancer Algorithm:
The HAProxy load balancer employs the Round Robin distribution algorithm. This dynamic algorithm ensures equitable distribution of processing time among servers by using them in turns based on their configured weights. Adjustments to server weights can be made on-the-fly, enhancing flexibility.

Load-Balancer Enabled Setup:
The HAProxy load balancer facilitates an Active-Passive setup, as opposed to an Active-Active configuration. In Active-Passive, not all nodes are actively receiving workloads simultaneously. The setup allows for standby nodes, ensuring that the next passive node becomes active when the preceding node is inactive.

Database Primary-Replica (Master-Slave) Cluster:
This setup designates one server as the Primary server capable of read/write operations and another as the Replica server restricted to read operations. Synchronization between the Primary and Replica servers occurs whenever the Primary executes a write operation.

Difference Between Primary and Replica Nodes:
The Primary node handles all write operations, while the Replica node processes read operations. This distribution decreases read traffic on the Primary node, optimizing overall system performance.

Issues With This Infrastructure:

Single Points of Failure (SPOF):
The infrastructure harbors multiple SPOFs, such as the Primary MySQL database server. If it experiences downtime, the entire site becomes unable to make changes. The servers housing the load balancer and the application server connecting to the primary database server also pose potential points of failure.

Security Concerns:
The absence of SSL encryption for transmitted data poses a security risk, enabling potential interception by hackers. Additionally, the lack of firewalls across servers leaves the infrastructure vulnerable to unauthorized access.

Monitoring Absence:
The absence of server monitoring tools denies visibility into the status of each server. Implementing monitoring mechanisms is essential to proactively address potential issues and ensure the overall health and performance of the infrastructure.