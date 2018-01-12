#!/bin/bash
## In order to verify the number of concurrent connections from all
## clients that are connected to your server, you can use the "netstat"
## command to count the total number of concurrent connections for each
## IP:
## $ netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
##      1 107.77.165.11
##      1 149.23.61.26
##      1 172.58.72.220
##      1 181.54.254.152
##      1 63.143.42.251
##      1 71.198.212.176
##
##      2 54.183.130.127
##      3 58.218.198.161
##      4 75.101.42.109
##      6 69.164.201.81
##      6 69.181.182.33
##      8 68.224.70.17
##     15 127.0.0.1
##    124 108.59.12.76
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n