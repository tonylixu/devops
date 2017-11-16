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
Even in solution2, we pre-calculate the sum of at each point, the time complexity is still O(n^2). Can we further improve the solution? Yes, we can. This time we can use the "sliding window" technique, which is very typical for array/list operations. Imaging we have a dynamic window frame, which the size of the window can be changed. Start from the begining of the array, we load each element and calculate the sum, if the sum is bigger than s, then we stop and mark it as min_len, then we decrease the left boundry of this window by one and moving forward.

This way, we could avoid the previous calcualted and non-working elements.

Example:
nums = [2,3,1,2,4,3] and s = 7
* step 1: both left and right boundry of our window is at position 0. sum = nums[0] = 2, 2 < 7
* step 2: right boundry is 1 and left boundry is still 0, sum = sum + nums[1] = 5, 5 < 7
* step 3: right boundry is 2 and left boundry is still 0, sum = sum + nums[2] = 5 + 1 = 6, 6 < 7
* step 4: right boundry is 3 and left boundry is still 0, sum = sum + nums[3] = 6 + 2 = 8, 8 > 7, the window size is "right boundry - left boundry + 1" = 4
* step 5: we done all the checks with nums[0], we move up left boundry by 1, now right boundry is 3 and left boundry is 1, and total becomes sum = sum - nums[left boundry] = sum - nums[0] = 8 - 2 = 6. Now left boundry is 1 and right boundry is 3
* Step 6: Move up the right boundry by 1, now right boundry is 4, left boundry is 1, sum = sum + nums[4] = 10 > 7, we set min_len to min(min_len, right boundry - left boundry + 1) which is still 4, now we done all the checks with nums[1], we move up left boundry, and now total becomes sum = sum - nums[1] = 10 - 3 = 7 and 7 >=7, left boundry is 2. Now the new min_len is min(min_len, right boundry - left boundry + 1) which is 3. We move up left boundry and calculate the new total, sum = sum - nums[2] = 6, left boundry is 3.
* step 7: Move up the right boundry by 1, right boundry is 5, left boundry is 3. sum = sum + nums[5] = 9, which is bigger than 7. Now min_len is min(min_len, right boundry - left boundry + 1) which is still 3. We move up left boundry and substract nums[3] from the total. sum = sum - nums[3] = 7, left boundry is 4 now. 7 is still >= 7, we calculate the min_len, min(min_len, right boundry - left boundry + 1) which is 2, so min_len is 2 now. We move up left boundry and substract nums[4] from the total. sum = sum - nums[4] = 5.
* step 8: Now sum is 5, left boundry is 4 and right boundry is 5, we reach the last element. We can exit now and return the result.
