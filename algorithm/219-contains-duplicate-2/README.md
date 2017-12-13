### Problem Definition
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that `nums[i] = nums[j]` and the absolute difference between i and j is at most `k`.

### Examples
```bash
nums = [1, 4, 5, 6, 8, 1, 8, 1], k=3
for element 1, indexs are 0, 5, and 7, differences are 5, 7 and 2.

Your code should return True since 2 <= 3
```