### Problem Definition
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

### Example:
```bash
Input: "Hello World"
Output: 5
```

### Problem Analysis
This is an easy one, we can generate a list by spliting the entire string on space, and output the length of last word. Watch for the edge case when list is empty or only contains spaces.
