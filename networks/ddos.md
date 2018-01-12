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

### How to Mitigate DDoS Attacks
Since we've identified the offending IP(s), now we can kill the connections and to stabilize the server. You can use the `tcpkill` command. This command is part of `dsniff` tool suite for Linux to sniff network traffic for cleartet insecurities.

Install "dsniff":
```bash
# apt-get install dsniff
```

Kill connections from host/IP:
```bash
# tcpkill host 138.59.12.763
tcpkill: listening on eth0 [host 138.59.12.763]
138.59.12.763:80 > 18.9.12.76:55131: R 3995187069:3995187069(0) win 0
138.59.12.763:80 > 18.9.12.76:55131: R 3995187313:3995187313(0) win 0
138.59.12.763:80 > 18.9.12.76:55131: R 3995187801:3995187801(0) win 0
18.9.12.76:55131 > 138.59.12.763:80: R 1852751082:1852751082(0) win 0
...
```

Block the IP in ufw:
```bash
# ufw deny from 138.59.12.763 to any
```

At this point, as you started to kill connections and block offending IPs, your web service should start recovering. You might need to restart your web service if necessary.

### How to Protect Future DDos Attacks?
Ubuntu comes bundled with UFW, which is an interface to iptable. This is basically a very lightweight router/firewall inside the Linux Kernel that runs way before any user applications.

### We will configure the following UFW rules:
* Rate limiting: A rate limit of x connections per y seconds means that if x connections has been initiated in the last y seconds by this profile, it will be dropped. Dropping is actually a nice protection against flooding because the sender won't know that you dropped it. He might think the packet was lost, that the port is closed or even better, the server is overloaded. Imagine how nice, your attacker thinks he succeeded, but in fact you are up and running, him being blocked.
* Connections per IP: A connection is an open channel. A typical browser will open around 5 connections per page load and they should last under 5 seconds each. Firefox, for example, has a default max of 15 connections per server and 256 total. I decided to go for 30 connections / 20 seconds / IP
* Connections per Class C: Same a above, but this time we apply the rule to the whole Class C of the IP because it is quite common for someone to have a bunch of available IPs. This means for example all IPs looking like 11.12.13.*. In our example, we go for 30 simultaneous connections.

### Configure UFW:
Update the "/etc/ufw/before.rules", add:
Add those lines after *filter near the beginning of the file
```bash
:ufw-http - [0:0]
:ufw-http-logdrop - [0:0]
```

Add those lines near the end of the file, before the "COMMIT":
```bash
### Start HTTP ###

# Enter rule
-A ufw-before-input -p tcp --dport 80   -j ufw-http
-A ufw-before-input -p tcp --dport 443  -j ufw-http

# Limit connections per Class C
-A ufw-http -p tcp --syn -m connlimit --connlimit-above 30 --connlimit-mask 24 -j ufw-http-logdrop

# Limit connections per IP
-A ufw-http -m state --state NEW -m recent --name conn_per_ip --set
-A ufw-http -m state --state NEW -m recent --name conn_per_ip --update --seconds 20 --hitcount 30 -j ufw-http-logdrop

# Finally accept
-A ufw-http -j ACCEPT

# Log
-A ufw-http-logdrop -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW HTTP DROP] "
-A ufw-http-logdrop -j DROP

### End HTTP ###
```

### Prevent Ping Flood
Make sure you don't get ping flood by setting some iptables rules that limit icmp. You can prevent ping/icmp flood with iptables add these rules right before the COMMIT.
```bash
-A INPUT -p icmp -m limit --limit 6/s --limit-burst 1 -j ACCEPT
-A INPUT -p icmp -j DROP
```

### Disable IPv6
You can also disable IPv6 if you are not using it:
```bash
# vi /etc/default/ufw
Set to "no"
IPV6=no
```

Finally, do a:
```bash
# ufw reload
```