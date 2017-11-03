## Problem Definition
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule ie that if two nodes overlap, then sum node values upas the new value of the merge node. Otherwise the None node will be used.

### Example1:
```bash
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
```

### Time complexity
O(n), n is the number of elements in the tallest tree

### Space complexity
O(n). Two binary trees