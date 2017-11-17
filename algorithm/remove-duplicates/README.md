### Problem definition
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

### Problem anaysis
You can use a dictionary, the key is the element in the array nums, and the value is the count. Then you iterate the whole array, one element at a time, if the element is in the key, counter plus one, if counter equals to 2, simple pass. Then output the sum of all the keys.
pesudo code:
```python
dc = {}
for i in nums:
    if i not in dc:
        dc[i] = 1
    elif dc[i] == 2:
        pass
    else:
        dc[i] += 1
total = []
for k,v in dc.items():
    while v > 0:
        total.append(k)
        v -= 1
nums = sorted(total)
return len(nums)
```