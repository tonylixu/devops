import json
from pprint import pprint

# Open data file and load into data dict
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

pprint(data)

# Just for fun, to try JSON dump
m = {'id': 2, 'name': 'hussain'}
n = json.dumps(m)
print type(n)