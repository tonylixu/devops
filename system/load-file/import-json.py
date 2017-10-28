import json
from pprint import pprint

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

pprint(data)