### Problem Definition
Given a non-empty string `s`, you may delete at most one character. Judge whether you can make it a palindrome.

### Examples:
```bash
Input: "aba"
Output: True

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

### Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

### Problem Analysis
Edge cases:
* String is empty or None -> return False
* String only contains lowercase characters
* The maximum length of the string is 50000

### Solution Analysis
We could check if a string is or contains a palindrome sub-string by going through the string itself, and each sub-strings, by removing one character each time, from the begining of the string.

We start from the full string `s`, then move on to `s[1:]`, `s[0:1] + s[2:]`... and so on.

The Python implementation is in `solution1.py`.

The time complexity of `solution1` is O(n^2), which exceed the time limit. The space complexity is O(3n). Not a very good implementation/solution.