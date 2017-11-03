
def partition(array, start, end):
    pivot = A[end]
    # Set partition index as start initially
    p_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            # Swap if element is less than pivot
            A[i], A[p_index] = A[p_index], A[i]
            p_index++
    # Swap pivot with element at partition index
    A[p_index], A[end] = A[end], A[p_index]
    return p_index