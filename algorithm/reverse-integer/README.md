## Probelm Definition
Reverse digits of an integer.
```bash
Example1: x = 123, return 321
Example2: x = -123, return -321
```
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

### Analysis
This problem is fairly simple. The only thing to watch out is the overflow. You need to pay attention to the input integer and also the revsered integer.

### Time Complexity
O(n), since the slice size is n

### Space Complexity
O(n), n is the number of the element