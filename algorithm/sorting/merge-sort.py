# Mergesort is a divideand conquer algorithm
# which means we break the problem into sub-problems and
# find solution to sub-problems, and from the solution to
# sub-problems we construct a solution of the actual problem.
# 
# Mergesort is a stable algorithm, it preserves the relative order
# of records with same key.
#
# Mergesort is not a In-place algorithm. The extra space it will take is
# propotional to the number of elements in the array

def merge_sort(array):
    # Only one element in the array, consider sorted
    if len(array) < 2:
        return array
    # Fidn the middle of the array
    mid = len(array) / 2
    array_l = array[:mid]
    array_l = merge_sort(array_l)
    array_r = array[mid:]
    array_r = merge_sort(array_r)
    array = merge(array_l, array_r)
    return array

def merge(al, ar):
    c = []
    while len(al) != 0 and len(ar) != 0:
        if al[0] < ar[0]:
            c.append(al[0])
            al.remove(al[0])
        else:
            c.append(ar[0])
            ar.remove(ar[0])
    if len(al) == 0:
        c += ar
    else:
        c += al
    return c
    

if __name__ == "__main__":
    cards = [2, 4, 1, 6, 8, 5, 3, 7]
    print merge_sort(cards)