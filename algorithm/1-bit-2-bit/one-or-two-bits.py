bits = [1, 0, 1, 0]
# Calculate the array length
length = len(bits) - 1
i = 0
while i < length:
    i += bits[i] + 1
if i == length:
    print True
else:
    print False