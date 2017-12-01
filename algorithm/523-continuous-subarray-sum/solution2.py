nums = [23, 2, 4, 6, 6]
k = 6
dmap = {0 : -1}
total = 0
for index,value in enumerate(nums):
    total += value
    m = total % k if k else total
    print "--------"
    print "index=" + str(index) + ", value=" + str(value)
    print "total=" + str(total) + ", m=" + str(m)
    if m not in dmap:
        dmap[m] = index
    elif dmap[m] + 1 < index:
        print True
    print dmap
# print dmap 