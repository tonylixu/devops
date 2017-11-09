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
But this solution failed the time complexity test.

After the second thought, read the problem defintion couple of times, I realize that `every element appears twice except for one`. What if you could cancle out all the identical elements by some operation, then the only one left would be the one that we are looking for. We can sort the array, then start from the first element, and moving forward. Pseudo code:
```bash
array = sorted(array)
for i in array:
    check array[i] with array[i+1]
    if array[i] == array[i+1]:
        array[i] = array[i+1] = 0
```
Does this ring the bell? Binary operations! The XOR opersation will return 0 if two elements are the same.
For example:
1 ^ 1 = 0
1234 ^ 1234 = 0
1234 ^ 1234 ^ 1 = 1
and order doesn't matter, so we don't even need to sort the array!
1234 ^ 1 ^ 1234 = 1

So there you go:
```bash
temp = 0
for a in array:
    temp ^= a
return temp
```

### Time complexity analysis
* Time complexity is O(n), n is the number of element in array
* Space complexity is O(n), n is the number of element in array
