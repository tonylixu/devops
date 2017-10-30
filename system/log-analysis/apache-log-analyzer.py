import re
#line = '64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846'
# Define the right regex for Apache log file
# We always use raw string notation for regex patterns
regex = '([(\d+)].+) - - \[(.*)\] "(.*)" (\d+) (\d+)'

with open('apache.log', 'r') as f:
    lines = f.readlines()
    
for line in lines:
    print re.match(regex, line).groups()