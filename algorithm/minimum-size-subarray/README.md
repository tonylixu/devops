### Problem Definition

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

### Problem analysis
Obvisouly we can use brute force solution on this one. We could generate all the sub strings, and calculate the sum, compare with s, then recored the minum. If there is no sum >= s, we simply return 0.

pseudo code:
```python
length = len(array)
    min_len = length + 1
    min_array = []
    for i in range(length):
        for j in range(i+1, length+1):
            total = 0
            temp_array = []
            for k in range(i, j):
                total += array[k]
                temp_array.append(array[k])
            if total >= s and min_len > len(temp_array):
                min_len = len(temp_array)
                final_array = temp_array
```