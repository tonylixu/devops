### Problem Definition
Write a function to find the longest common prefix string amongst an array of strings.

### Example
```bash
Given strs = ["hello", "heaven", "heavy"]

Return "he"
```

### Problem Analysis
Edge cases:
* strs is empty, return ""
* There is no common prefix, return ""

### Solution analysis
We can use the first string of the strs, for each element in the string, we check the rest of the strings:
* If the length of each string is bigger than the index and the element of each string at index is equal, we move on, otherwise we return at string[i]
* Return true if the loop finishes