## Time Complexity
What is the time complexity of the following code:
```bash
int j = 0;
    for(int i = 0; i < n; ++i) {
        while(j < n && arr[i] < arr[j]) {
            j++;
        }
    }
```

Time complexity is O(n). Even in the first look, the time complexity seems to be O(n^2) due to two loops, however, the variable j is not initialized for each value of variable i.

Hence, the inner j++ will be executed at most n times. The "i" loop also runs n times, so the whole thing runs for O(n) times.

Lets assume the array passed has its element in decreasing order. We will just dry run through the code :
```bash
[10, 9, 8, 7 , 6, 5, 4, 3, 2, 1]
step 1: i=0, j=0, arr[0] < arr[0] is false, so the inner while loop breaks.
step 2: i=1, j=0, arr[1] < arr[0] is true, j=1.
step 3: i=1, j=1, while loop break. Note that j will remain 1 and is not reset back to 0.
step 4 : i = 2, j = 1. arr[2] < arr[1]. True. j = 2.
step 5 : i = 2, j = 2. Condition false. Break.
step 6 : i = 3, j = 2. arr[3] < arr[2]. True. j = 3.
step 7 : i = 3, j = 3. Condition false. Break.
```
As you can see, the inner while loop only runs once in this case.
So, total iterations is 2 * N.