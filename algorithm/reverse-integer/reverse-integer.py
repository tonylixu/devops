x = int(-3432432)
overflow = (1 << 31) - 1

# We got an overflow!
if abs(x) > overflow:
    print 0

# Convert x to list
list_x = list(str(x))
negative = 0
if '-' in list_x:
    negative = 1
    list_x.remove('-')
new_x = int(''.join(list_x[::-1]))
new_x = -1 * new_x if negative else new_x
if abs(new_x) > overflow:
    print 0
print new_x