bits = [1, 0, 0]
# Calculate the array length
length = len(bits) - 1
i = 0

# Iterate the whole array till the last element
while i < length:
    # If bits[i] == 0, we move 1
    # else we move 2
    # 
    i += bits[i] + 1
# If we have one element left
if i == length:
    print True
else:
    print False