### Problem definition
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
```python
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
```

Example 2:
```python
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

### Problem analysis
* The array contains a list of non-negative numbers, we are looking for a sub-array which it is sum is the multiple of k (sum % k == 0). 
* Edge cases:
  * Length of array is <= 10,000, return False if length > 10,000
  * If array is empty, return False
  * If k is negative, return False
  * Assume the sum of all numbers is <= 2^31
* Are we allow to change the array?
* How often do we encounter this kind of issue?

### Solution1
We can traverse the whole list, starting from index `0`, and calculate the sum of [i1, i2], [i1, .. i3] and so on. If there is no solution for index i, we simplely repeat the process from index i+1. Return True if we find a subarray, return False if no such a array exist.

The time complexity of solution1 is O(n^2)

### Solution2
Solution1 works, but it has a time complexity of O(n^2) and it will probably exceed the time limit on very big list. We can optimize the soltuion by using a mathmetical way.

