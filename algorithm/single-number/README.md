## Problem Definition
Given an array of integers, every element appears twice except for one. Find that single one.

### Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

### Solution analysis:
For the first take, it really looks like a simple problem, but the challenge comes when the array becomes very big, can your solution have as less time complexity as possible, without using extra memories?

My first solution was:
```bash
for i in array:
    if array.count(i) == 1:
        return i
```