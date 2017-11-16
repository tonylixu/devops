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
for i in range(length):
    for j in range(i+1, length+1):
        total = 0
        for k in range(i, j):
            total += array[k]
        if total >= s:
            min_len = min(min_len, j-i+1)
```

The time complexity of the brute force solution is O(n^3) and space complexity is O(1)

### Solution2:
We can use the sacrifies some spaces to gain some speed. We could pre-calculate the sums of elments at each point, and store it in an array for later use. This way we don't need to calculate sums in a loop each time.

pseudo code:
```python
length = len(nums)
min_len = length + 1
pre_sum = [0] * length
pre_sum[0] = nums[0]
for i in range(length):
    pre_sum[i] = pre_sum[i-1] + nums[i]
for i in range(length):
    total = 0
    for j in range(i, length):
        total = pre_sum[j] - pre_sum[i] + nums[i]
    if total >= s:
        min_len = min(min_len, (j-i+1))
print min_len
```
The time complexity for solution2 is O(n^2), but the space complexity is O(n) now.

### Solution3:

