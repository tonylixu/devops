from __future__ import print_function
import time
import requests

urls = [one_line.strip() for one_line in open('urls.txt')]
length = {}
start_time = time.time()

for url in urls:
    response = requests.get(url)
    length[url] = len(response.content)

for k,v in length.items():
    print("{0:30}: {1:8,}".format(k, v))

end_time = time.time()
total_time = end_time - start_time
print("\nTotal time: {0::.3} seconds".format(total_time))
