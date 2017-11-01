## Problem Definition
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

### Examples:
Example 1:
```bash
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
```

Example 2:
```bash
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
```

Note:
* 1 <= len(bits) <= 1000.
* bits[i] is always 0 or 1.

### Analysis
To solve this problem, you need to find iterate the whole list and find the pattern. It is important that we iterate the whole list from the very begining, don't sort or start from the middle because it is pointless. When you at the `i`th element, if the ith element is a `0`, this tells you the current character must be a `1` bit character, and if the ith element is a `1`, then the current character must be a `2` bits character.

For example, give an list of a=[0, 1, 0]. Start from a[0], which is a `0`, so the first character is a `1` bit. Then we move the index by `1`. a[1] is `1`, which tells us that this is a two bits character, so we move the index by `1`. After this step, index will become 3 which is the length of the array (We are at the end). So we stop, and return False. Another example is, given a=[1, 0, 0], by use the same strategy, we can tell that the last character is a `1` bit character, and the index will be `2` and equals the length of array - 1, this tells us we are at the `-1` postition and there is only one and one bit character left, so we return True.