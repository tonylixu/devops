gi
def quicksort(array, start, end):
    if start < end:
        p_index = partition(array, start, end)
        quicksort(array, start, p_index-1)
        quicksort(array, p_index+1, end)
    return array

def partition(array, start, end):
    pivot = array[end]
    # Set partition index as start initially
    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            # Swap if element is less than pivot
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    # Swap pivot with element at partition index
    array[p_index], array[end] = array[end], array[p_index]
    return p_index

if __name__ == "__main__":
    array = [7, 2, 1, 6, 8, 5, 3, 4]
    print quicksort(array, 0, 7)