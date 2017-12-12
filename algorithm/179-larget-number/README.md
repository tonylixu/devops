t p### Problem Definition
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given `[3, 30, 34, 5, 9]`, the largest formed number is `9534330`.

Note: The result may be very large, so you need to return a string instead of an integer.

### Problem Analysis
We can sort the array, by useing a special compare function. For given two strings a and b:
```python
if a + b > b + a:
    return -1
else:
    return 1
```
 p
The key here is, since we are comparing the str version of sum, the `+` will concatenate two strings together. For a given two strings `121` and `12`(`['121', '12']`), apparently we should sort it to (`['12', '121']`), because `12112` is small than `12121`. So the lambda function here, is to help us to define the comparison mechnisam.

```python
if a + b > b + a:
    return -1
else:
    return 1
```
In our example, `a` is `121`, `b` is `12`, `a+b` is `<` then `b+a`. So `1` is returned. In a compator context, `1` means the first argument `121` is condidered bigger than the second argument `12`, so `121` should be placed after `12`.

The time complexity of the sorting is O(nlogn)