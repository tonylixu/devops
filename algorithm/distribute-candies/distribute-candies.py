a = [1,2,3,4,5,6,7,8,9,10]
length = len(a)
# We count element differences
set_a = set(a)
kinds = len(set_a)
if kinds == length/2:
    print kinds
elif kinds < (length/2):
    print kinds
else:
    print length/2