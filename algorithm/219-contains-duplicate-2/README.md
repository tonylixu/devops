### Problem Definition
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that `nums[i] = nums[j]` and the absolute difference between i and j is at most `k`.

### Examples
```bash
nums = [1, 4, 5, 6, 8, 1, 8, 1], k=3
for element 1, indexs are 0, 5, and 7, differences are 5, 7 and 2.

Your code should return True since 2 <= 3
```

### Problem Analysis
Edge cases:
* array size is 0 -> return False
* k is negative or equals 0 -> return False
* array has 1 element -> return False
* array elments are all the same -> depends on k


### Solutiuon Analysis
We could use a dictionary, which `k` is the array element and value is the index. Then we traverse the whole array once, for each element, we check if the element exists in the dictionary and calculate the diffrence between the current index and the index saved in the dictionary.

If the element doesn't exist, we add it into the dictionary, else if the difference qualifies, we return `True`, otherwise we update the value index to be the current index and move on to the next element.

If at the end there's no element qualifies, we return False. 