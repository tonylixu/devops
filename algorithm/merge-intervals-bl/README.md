### Problem defintion
Given a collection of intervals, merge all overlapping intervals.

Examples:
```python
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
```

### Problem questions
* Is the list/array sorted? Can the array be sorted?
* Am I allow to create new lists?
* What are the edge cases? How big is the list, any negative numbers, what if the array length is 0 and 1.
* Am I allow to use python embededed functions?


### Draft solution
If we can sort the whole list, we sort the list first, so that we don't need to worry about elements that already been merged. Once the list is sorted, We can start solving this problem by creating a new list, extract each element from old one, merge into the new list. If the new element doesn't overlap with the existing ones, simply append the new element. Otherwise merge it. This way, the new list is sorted and merged overlaps at any given time.

### Solution analysis
The time complexity of `solution.py` is O(nlogn), that's the time complexity of Python sort function. The traverse time of the whole list is O(n), where `n` is the number of elements.

### Optimization
The time complexity is O(nlogn), I am pretty happy with it, let's focus on the space complexity. In `solution1.py`, we created a merged_intervals list, which consumes extra spaces. We can probably use less space complexty by using pointers.

The idea here, is to use `pre` and `cur` pointers. `pre=0` and `cur=1` (if array length is >= 2, we still need to sort the array). Then we compare `pre.end` with `cur.start`, if `cur.start` is <= `pre.end`, we merge two and move `cur` forward by one, otherwise, `pre++` and `cur++`.
