## Which loop completes the fastest?
In a competition, four different functions are observed. All the functions use a single for loop and within the for loop, same set of statements are executed. Consider the following for loops:
```bash
A) for(i = 0; i < n; i++) O(n)
B) for(i = 0; i < n; i += 2) O(n/2)
C) for(i = 1; i < n; i *= 2) O(logn)
D) for(i = n; i > -1; i /= 2) Infinite
```