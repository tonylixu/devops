## Problem Definition
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Exmaple1:
```bash
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
```

Example2:
```bash
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies.
```

Notes:
* The length of the given array is in range [2, 10,000], and will be even.
* The number in given array is in range [-100,000, 100,000].

### Solution
The key point here is to find how many different kind of candies do you have in your candie jar. Once you find out the different number of candies you have, then you almost find the solution.

Another important part is to realize that no matter how many kinds of candies you have, the most different kinds number of candies you can give to the sister is <= (half length of the candies), you have to be fair :)

For exmaple, let's say you have 10 candies. If you have 10 different kinds of candies, you can only give 5 to your sister. If you have 4 different candies, you can give 4 different kinds of candies to your sister. If you have 1 different candies, you can give only give one. See the pattern here?

```bash
if kinds_of_candies <= half_of_length:
    return kinds_of_candies
else:
    return half_of_length
```

### Complexity
Time complexity: O(n), n is number of integers.
Space compleity: O(n), n is number of integers.