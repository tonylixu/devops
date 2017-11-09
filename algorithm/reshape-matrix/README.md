## Problem Definition
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

### Examples:
```bash
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
```

```bash
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```

### Solution analysis
* Questions:
  * What's the maximum rows and columns?
  * What will happen if the given rows and columns are negative
  * In the base matrix, does every list have equal length?
  * What happens if the base matrix has 0 element?

* Steps:
  * Make sure the base matrix is reshape-able
  * Combine all the list into a big list
  * Start filling into the new array
