### Problem definition
Given a string, find the length of the longest substring without repeating characters.

### Examples
* Given "abcabcbb", the answer is "abc", which the length is 3.
* Given "bbbbb", the answer is "b", with the length of 1.
* Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Solution analysis
Solution1:

The simplest way of solving this is the brute force way. We simply consider all substrings of s one by one, and pick up the one that has the longest length and contains all unique values.

To find all the substrings:
```python
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print s[i]..s[j]
a
ab
abc
abca...
```