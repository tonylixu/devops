# Time Complexity: O(m * n * logn)
#     (n*logn) is the sorted function time complexity
# Space complexity:
# 2*m*n
from collections import defaultdict

data = ['trees', 'bike', 'cars', 'steer', 'arcs']
d2 = defaultdict(list)
for w in data:
    d2[''.join(sorted(w))].append(w)
for l in d2.values():
    print l