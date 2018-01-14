## What is TCP SYN flooding Attacks

TCP SYN Flooding is a specific type of DDoS. This attack exploits an implementation characteristic of the TCP protocol, and can be used to make server processes incapable of resposing a legitimate client request for new TCP connections. Any service that binds to and listens on a TCP socket is potentially vulnerable to TCP SYN flooding attacks.

### The TCP Three-way Handshake
The basis of SYN flooding attack lies in the design of the 3-way handshake of TCP protocol. When a client attempts to start a TCP connection to a server, the client and server exchange a series of messages in the following sequences:
1. Client request a connection by sending a SYN message to server.
2. Server acknowledges the message and send back a SYN-ACK to client.
3. The client responds with an ACK, and the connection is established.

This is called TCP "Three-way" handshake. Every TCP connection established uses it.

### Transmission Control Block (TCB)
During the TCP transmission, the TCB (Transmission Control Block) data structure is being used. TCB holds all the information about a connection. Each TCB size exceeds at least 280 bytes. Very importantly, TCB is allocated based on the reception of the SYN packet before the connection is fully established. This leads to a very clear potential DDoS attack, where the incoming SYNs cause the allocation of huge amount of TCBs that exhaust the server's resources. When this happens, the server continues to wait for acknowledgement for each of the requests (which on the client side ACKs are ignored so there is no ACKs ever), binding resources until no new connections can be made, and ultimately resulting in denial of service.

### Symptoms
When an attack starts, the server sees the equivalent of multiple attempts to establish TCP communications. The server also responds to each attempt with a SYN/ACK (synchronization acknowledged) packet from each open port, and with a RST (reset) packet from each closed port. Since this is SYN attack, the client never sends back the ACK packet, instead the clinet probably discard all the ACK-SYN recevied and keep sending SYNs to the server. Server will have to wait certain amount of time to close these half-opened connections. Eventually the TCP backlog is full and server denies any new connections.

### Defense against syn flood attacks
Firewall: Iptables is the default firewall for Linux computers.The rule of thumb: block all the incoming traffic except the traffic you REALLY need on your server. Allow management only from trusted sources.
The easiest case is an attack from one host without IP spoofing. It is easy to eliminate:
```bash
# iptables -A INPUT -p tcp -m state --state NEW -m recent --update --seconds 20 --hitcount 20 -j DROP
# iptables -A INPUT -p tcp -m state --state NEW -m recent --set -j ACCEPT
```
The above two rules limite the rate of SYN requests from a single IP to 20 per 20 seconds. If the rate limit it too high, adjust it your to your own.
```bash
iptables -t mangle -I PREROUTING -p tcp -m tcp --dport 80 -m state --state NEW -m tcpmss ! --mss 536:65535 -j DROP
```
Some SYN attacks have `unusal` parameters in the TCP header. The first one is MSS (Maximum Segment Size) – maximum size of the segment that a host initiating the connection wants to allow. Most attacking tools (including hping) do not set this parameter by default. Most of legitimate client set it on the other hand. The normal value is between 536 and 65535.

### Update Linux kernel parameters
* Increasing TCP backlog: This is a poor solution, should not be seriously considered unless in a urgent situation. The attacker can always scale to large orders to get it fill again.
```bash
# echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog
## To make it permantelly
# vim /etc/sysctl.conf
add
net.ipv4.tcp_max_syn_backlog = 2048
```
* Enable SYN cookies. SYN cookie is a technique used to resist SYN flood attacks. In particular, the use of SYN cookies allows a server to avoid dropping connections when the SYN queue fills up. Instead, the server behaves as if the SYN queue had been enlarged. The server sends back the appropriate SYN+ACK response to the client but discards the SYN queue entry. If the server then receives a subsequent ACK response from the client, the server is able to reconstruct the SYN queue entry using information encoded in the TCP sequence number. [SYN cookies](https://en.wikipedia.org/wiki/SYN_cookies)
```bash
# echo 1 > /proc/sys/net/ipv4/tcp_syncookies
# echo 3 > /proc/sys/net/ipv4/tcp_synack_retries
## To make it permantelly
# vim /etc/sysctl.conf
addnet.ipv4.tcp_syncookies = 1
net.ipv4.tcp_synack_retries = 3
```

### Protection using Switches
Most switches have some rate-limiting and ACL capability. Some switches provide automatic and/or system-wide rate limiting, traffic shaping, delayed binding (TCP splicing), deep packet inspection and Bogon filtering (bogus IP filtering) to detect and remediate denial of service attacks through automatic rate filtering and WAN Link failover and balancing.

### Using Commercial tools and services
There are commercially available tools and services to protect. For example, Cloudflare, Prolexic, Incapsula, Arbor Networks, Fortinet etc. If your business is very critical, then it worth to pay the $$.

### Using IDS and IPS
Install Intrusion detection systems (IDS) and Intrusion Prevention systems(IPS) in your server. There are plenty of great IDS and IPS available in the market. If you are a small or medium business that can’t afford commercial solutions, then there is a free alternative for you. Snort is a free and open source IDS/IPS that is freely available to everyone. You can configure snort to block all kinds of DoS attacks.