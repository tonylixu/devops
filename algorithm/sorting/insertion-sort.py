
def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        value = array[i]
        hole = i
        while hole > 0 and array[hole-1] > value:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole] = value
    return array

if __name__ == "__main__":
    cards = [2, 4, 7, 1, 5, 3]
    print insertion_sort(cards)