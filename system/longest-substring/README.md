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
abca
abcab
abcabc
abcabcb
abcabcbb...
```

This solution is very simple and straight forward, but it also has a big time complexity, the Big O is O(n^3). If you take a close look of the substrings, you can see that we are doing a lot of duplcation checks. For example, "abca", "abcab", "abcabc", ... before we check "abcabc", we already checked "abca" and "abcab" and already know that they both are not the answers, so "abcabc" check is unnecessary. Therefore, we introduce the "sliding window" approach.

Solution2:

"Sliding window". This is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices. i.e [i, j) (left-closed, right-open). A sliding window is a window "slides" its two boundries to the certain direction. For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1).

Our new solution can use this "sliding window" straetegy. We use hashset to store the characters in the current window. Then we slide the index j to the right. If it is not in the Hashset, we slide j further. Keep doing so until s[j] is already in the hashset. At this point, we found the maximum size of substrings without duplicate.