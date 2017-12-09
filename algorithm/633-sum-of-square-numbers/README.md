### Problem Definition
Given a non-negative integer `c`, your task is to decide whether there're two integers a and b such that `a^2 + b^2 = c`.

### Exmaple 1:
```bash
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
```

### Example 2:
```bash
Input: 3
Output: False
```

### Solution Analysis:
The simplest solution would be to consider every possible combination of two integers and check if the sum of their squares equals `c`. Since both a and b must lie within the range of `(0, sqrt(c))`, we only need to verify the values of `a` and `b` in this range only.