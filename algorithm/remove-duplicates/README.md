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
Time complexity is O(n), space complexity is also O(n)

### Solution2
Use pointers. We can use `p` and `c` two pointers. Starts from element 1 and 2. `p = 1`, `c = 2`. For each `c`, we compare `c` with `p` and `p-1`, if equals, we move `c = c+1`, and compare again. If not equals, we swap `p+1` with `c`, and `p = p+1`. This way, all repated more than twice elements are swaped to the end of the array. We simply return `p+1`.
pseudo code:
```python
if len(nums) <= 2: return len(nums)
    p = 1; c = 2
while c < len(nums):
    if nums[c] == nums[p] and  nums[c] == nums[p-1]:
        c += 1
    else:
        p += 1
        nums[p] = nums[c]
        c += 1
return p + 1
```
Time complexity is O(n), space complexity is O(n)