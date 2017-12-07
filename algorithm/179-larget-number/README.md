### Problem Definition
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given `[3, 30, 34, 5, 9]`, the largest formed number is `9534330`.

Note: The result may be very large, so you need to return a string instead of an integer.

### Problem Analysis
We can sort the array, by useing a special compare function. For given two strings a and b:
```python
if a + b > b + a:
    return -1
else:
    return 1
```

The time complexity of the sorting is O(nlogn)