from __future__ import print_function

import requests
import time
import threading
from queue import Queue

urls = [one_line.strip() for one_line in open('urls.txt')]
queue = Queue() # Thread safe queue
start_time = time.time()
threads = []

# Define a get url content length function
def get_length(url):
    response = requests.get(url)
    queue.put((url, len(response.content)))

# Launch our function in a thread
print("Launching thread...")
for url in urls:
    t = threading.Thread(target=get_length, args=(url,))
    threads.append(t)
    t.start()

# Joining all
print("Joining all threads...")
for thread in threads:
    thread.join()

# Collect length and print
print("All url lenth:")
while not queue.empty():
    url, length = queue.get()
    print("{0:30}: {1:8,}".format(url, length))

end_time = time.time()
total_time = end_time -­ start_time
print("\nTotal time: {0:.3} seconds".format(total_time))
