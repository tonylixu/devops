#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

#arr = [
#    [-1, -1, 0, -9, -2, -2],
#    [-2, -1, -6, -8, -2, -5],
#    [-1, -1, -1, -2, -3, -4],
#    [-1, -9, -2, -4, -4, -5],
#    [-7, -3, -3, -2, -9, -9],
#    [-1, -3, -1, -2, -4, -5]
#]

index = [3,4,5,6]
max_value = -100000000
for k,v in enumerate([3,4,5,6]):
    sub_arr = [[row[i:i+3] for row in arr[k:v]] for i in range(4)]
    for sa in sub_array:
        max_value = max(max_value, (sum(sa[0]) + sa[1][1] + sum(sa[2])))
print max_value
