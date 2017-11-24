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

