### Problem Definition
Given a  2D Array, A:
```bash
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
We define an hourglass in A to be a subset of values with indices falling in this pattern in 's graphical representation:
```bash
a b c
  d
e f g
```
There are  hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task: Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Constraints:
* -9 <= A[i][j] <= 9
* 0 <=i,j <=5

Output:
* Print the largest (maximum) hourglass sum found in A.

Example:
```bash
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Output:
19
```

Explanation:
```bash
A contains the following hourglasses:
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum(19) is:
2 4 4
  2
1 2 4
```