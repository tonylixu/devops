## Quick Sort
Quick sort is a in-place sorting algorithm, which means it takes constant of memory. The average time complexity of quick sort is O(nlogn), but the worst case time complexity is O(n^2). Quick sort is also a recursive sorting algorithm.

Quick sort is pretty fast in practical scenarios. It is often the most poractical and choices for sorting.


### Suedo code
```python
def quicksort(A, start, end):
    if start < end:
        return
    p_index = partition(A, start, end)
    quicksort(A, start, p_index-1)
    quicksort(A, p_index+1, end)

def partition(A, start, end):
    # Alwasy select the right most element as pivot
    pivot = A[end]
    p_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            swap(A[i], A[p_index])
            p_index += p_index
    swap(A[p_index], A[end-1])

A[7, 2, 1, 6, 8, 5, 3, 4]
start = 0, end = 7
Step 1:
pivot = 4, p_index = 0
Now we push all the emlements that smaller than 4 to the left of pivot
i = 0, A[i] = 7, and A[i] > pivot, no swap will happen
A[7, 2, 1, 6, 8, 5, 3, 4]

Step 2:
pivot = 4, p_index = 0
i = 1, A[i] = 2, and A[i] < 4, swap(A[i], A[p_index]) A[1], A[2]
p_index = 1
A[2, 7, 1, 6, 8, 5, 3, 4]

Step 3:
pivot = 4, p_index = 1
i = 2, a[i] = 1, and A[i] < pivot, swap(A[i], A[p_index]) A[2], A[1]
p_index = 2
A[2, 1, 7, 6, 8, 5, 3, 4]

Step 4:
pivot = 4, p_index = 2
i = 3, A[i] = 6, and A[i] > pivot, no swap will happen
A[2, 1, 7, 6, 8, 5, 3, 4]

Step 5:
pivot = 4, p_index = 2
i = 4, A[i] = 8, and A[i] > pivot, no swap will happen
A[2, 1, 7, 6, 8, 5, 3, 4]

Step 6:
pivot = 4, p_index = 2
i = 5, A[i] = 5, and A[i] > pivot, no swap will happen
A[2, 1, 7, 6, 8, 5, 3, 4]

Step 7:
pivot = 4, p_index = 2
i = 6, A[i] = 3, and A[i] < pivot, swap(A[i], A[p_index]) A[6], A[2]
p_index = 3
A[2, 1, 3, 6, 8, 5, 7, 4]

Step 8:
pivot = 4, p_index = 3
i = 7, i > end -1, exit the for loop

Now all the element on the left of p_index (3) is smaller than the pivot [2, 1, 3], and all the elements on the right of p_index is greater than the pivot.

Now we sawp the A[p_index] with A[end], after this
A[2, 1, 3, 4, 8, 5, 7, 6]
```