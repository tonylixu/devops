### Problem definition
Given a string, find the length of the longest substring without repeating characters.

### Examples
* Given "abcabcbb", the answer is "abc", which the length is 3.
* Given "bbbbb", the answer is "b", with the length of 1.
* Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Solution analysis
We can start solving this problem by traverse the whole array/list. For each element we iterate, append it to a new array(list) if it doesn't exist in the new array/list already.

