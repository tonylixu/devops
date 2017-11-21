### Problem definition
Given an array, find if the sum of sub-array1 is equal to the sum of the sub-array2. Assume the array length is even, and it can be divided into two arrays. The length of array is equal to the length of sub-array1 plus sub-array2. 

For example:
```bash
nums = [1, 1, 2, 4]
Your program should print [1, 2, 3] and [4] 
```

Notes: Assume there are at least two elements in the array


### Problem analysis
We could use a pointer, traverse the whole array, at each point, we calculate the sum of left side (including the pointer value) and the sum of the right side. Then we compare the sum, if they equal, then we find the magic point.

### Solution 1
Please consult solution1.py for code implementation. The time complexity for this solution is O(n^2), even though we only traverse the whole array once, but the num() function time complexity is O(n). We do not use any extra spaces.