### Analysis
We could solve this problem by finding all the hourglasses in the array, calculate the sum and compare.

Remeber the list comprehension in Python? You could use list comprehension in this problem. To remind you, let's consider the following example:

```python
matrix = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12]]

[[row[i:i+3] for row in matrix] for i in range(4)]

gives you

[
[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
[[2, 3, 4], [5, 6, 7], [8, 9, 10]],
[[3, 4, 5], [6, 7, 8], [9, 10, 11]],
[[4, 5, 6], [7, 8, 9], [10, 11, 12]]]
```

Got the idea? Now checkout the `solution.py`

The time complexity of the solution is O(n), even though we have a second for loop, but it constant, always loop 3 times.
