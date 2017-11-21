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

You could further improve the time complexity to O(n) by only calculate the half sum of the array. See solution2

### Solution 2
We pre-calculate the half sum of the whole array. If the whole array contains two sub arraies that have the same sum, the total sum of the array itself can be divided by 2. As we traverse the array, we use a total variable to save the current sum. If there is a point the sum equals to half of the sum(array)/2, then we find the point. If at one point the sum of total is greater than sum(array)/2, there is no solution. See `solution2.py`

The time complexity is O(n), space complexity is still O(n)