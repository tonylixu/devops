## Ubuntu - How to Troubleshoot and Prevent DDOS Attack

A Distributed Denial of Service (DDoS) attach is an attempt to make an online service unavailable by overwhelming it with traffic from multiple sources. Banks, popular websites are the usual victims.

Attackers build "botnets" (a collection of infected computers), by spreading malicious software through emails, websites and social media. One a computer is infected, it can be controlled remotely and used like an army to launch attacks. Botnets can generate huge floods of traffic to overwhelm a target. These floods can be generated in multiple ways, such as sending more connection requests than a server can handle, or sending large amount of data to use up the bandwidth.

### There are four common categories of attacks:
* TCP Connection Attacks - Occupying connections. These attempt to use up all the available connections to infrastructure devices such as load-balancers, firewalls and application servers. Even devices capable of maintaining state on millions of connections can be taken down by these attacks.
* Volumetric Attacks - Using up bandwidth. These attempt to consume the bandwidth either within the target network/service, or between the target network/service and the rest of the Internet. These attacks are simply about causing congestion.
* Fragmentation Attacks - Pieces of packets. These send a flood of TCP or UDP fragments to a victim, overwhelming the victim's ability to re-assemble the streams and severely reducing performance.
* Application Attacks - Targeting applications. These attempt to overwhelm a specific aspect of an application or service and can be effective even with very few attacking machines generating a low traffic rate (making them difficult to detect and mitigate).

### How to Identify You Are Under DDos Attack
The immediate impact of DDoS attack is the slowness of your website or applications. If it takes a long time for you to connect to the web service and refresh takes minutes, you are probably under attack. To verify, log into your server as root, and check the number of concurrent connections from each IP address:
```bash
# netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
##      1 167.77.165.11
##      1 169.23.61.26
##      1 172.58.722.220
##      1 181.54.254.152
##      1 633.143.422.251
##      1 731.198.232.176
##      2 534.183.130.127
##      3 538.218.198.161
##      4 725.101.42.109
##      6 639.164.201.813
##      6 639.181.182.333
##      8 628.224.70.173
##     15 1227.0.0.1
##    124 138.59.12.763
```
In the above example, the offending IP is "138.59.12.763" with 124 connections. Sometimes attacks are from several IPs, so you might see a small total connection number, but a large list of IPs.