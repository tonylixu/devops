# Time complexity: O(n)
# Space complexity: 2 * n
numbers = [1, 2, 3, 5, 6, 8, 25]
numbers2 = []

length = len(numbers)
# Found flag
found = False

for i in range(length):
    numbers2.append(numbers.pop(0))
    if sum(numbers2) == sum(numbers):
        print "Number of steps is " + str(i+1)
        found = True
        break

if not found:
    print("Array disqualified")