### Problem definition
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,

Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
* You may assume k is always valid, 1 ≤ k ≤ array's length.

### Problem analysis:
* Is it possible the given array is an empty array?
* Any other constraints I should be aware of?
* What are the edge cases here?
* Can I sort, destroy or create new arrays?

### Solution analysis
The simplest solution for this one is just to sort the array then output the second last element.