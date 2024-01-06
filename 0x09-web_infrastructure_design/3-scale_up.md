
Description:

This upgraded web infrastructure represents a scaled-up iteration of the previously described system. Notably, all Single Points of Failure (SPOFs) have been eliminated, and each major component—web server, application server, and database servers—now resides on distinct GNU/Linux servers. SSL protection is not terminated at the load balancer, and each server's network is fortified by an individual firewall. Furthermore, comprehensive monitoring is implemented across the infrastructure.

Specifics About This Infrastructure:

Firewall Implementation:
Each server is equipped with its own firewall, providing individualized protection against unwanted and unauthorized users. This distributed firewall setup enhances the security posture of each server independently.
Issues With This Infrastructure:

High Maintenance Costs:
The transition to individual servers for major components raises maintenance costs significantly. The procurement of additional servers contributes to an increase in both upfront and ongoing expenses. This includes the expenditure on new servers, as well as the elevated electricity consumption required to sustain the operation of the expanded server fleet. Allocating funds for server acquisition and covering the heightened electricity bills becomes a necessary consideration for the company, potentially impacting its budget allocation.