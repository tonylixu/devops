### Problem definition
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example:
Given [[0, 30],[5, 10],[15, 20]],
return false.

### Problem analysis
Define the `false` situation. As long as the time interval of any two meetings has an overlap, there is a confilit. For example:
i1 =[2, 6] and i2 = [3, 8]

We see a conflict here, because i1 finishes before i2 finishes and after i2 starts. So as long as the minimum finish time of two meetings is larger than the maximum starting time, there is a conflict.

* Is there any time complexity constraints?
* Are we allow to modify the array or make new arrays?
* What happens if array is empty?
* What are the edge cases?
* Can we sort the array?
* Would brute force solution work?

### Solution1:
Alwasy the simplest soution, which is brute force, follow the KISSS principle :). We traverse the whole list and go through each sub list, and compare one by one, if we find an overlap, return false. Othersise return True at the end.

The time complexity of this solution is O(n^2) and space time complexity is O(n). n is the number of element.
pseudo code
```python
for i in range(len(intervals)):
    for j in range(i+1, len(intervals)):
        if min(intervals[i].end, intervals[j].end) > max(intervals[i].start, intervals[j].start):
            return false
return true
```

### Solution2:
We can further decrease the time complexity to O(nlogn) by sorting the list first then traverse the list. Because python sort function time complexity is O(nlogn) and traverse the whole list is n, so the total time complexity is O(nlogn).

