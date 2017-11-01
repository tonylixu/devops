# Time complexity: O(n^2)
# Space complexity: O(n)

def selection_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(i+1, length):
            if array[i] > array[j]:
                (array[i], array[j]) = (array[j], array[i])
    return array

if __name__ == "__main__":
    cards = [2, 7, 4, 1, 5, 3]
    print selection_sort(cards)
