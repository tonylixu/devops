### Problem definition
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

### Example:
```bash
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
```
Note: The input number n will not exceed 100,000,000. (1e8)

### Problem analysis
* What should be returned if the integer is negative - False
* What should be return if the integer is bigger than 100,000,000 - False

### Solution analysis
We can start with number `2`, and test ervery number, if it is dividable by N, then we save it, after checked everynumber, we calculate the sum, and compare with the number itself. If the sum equals the number, we return True.

`solutiuon1.py`