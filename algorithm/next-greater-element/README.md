### Problem definition
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

### Examples
Example 1
```python
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

Example 2
```python
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
```

Notes:
* All elements in nums1 and nums2 are unique.
* The length of both nums1 and nums2 would not exceed 1000.

### Solution analysis
We can traverse nums1 array, for each element, we find its position in nums2. If it is the last element, we return `-1`, otherwise we compare it with the rest of right element in nums2.

In Python, you can use the list index() function to find the elements index.

### Pesudo code
```python
# Traverse through the first array
for i in nums1:
    index = nums2.index(i)
    # Place holder if we find the numer
    find_it = 0
    # If it is the last element
    if index == len(nums2) - 1:
        re.append(-1)
    else:
        # Traverse the rest of right array
        for j in range(index+1, len(nums2)):
            if i < nums2[j]:
                re.append(nums2[j])
                find_it = 1
                # Until we find one
                break
        # If no find in the rest of right array
        if find_it == 0:
            re.append(-1)
    return re
```

### Complexity analysis
* Time complexity O(n^2)
* Space complexity O(n)