def remove_duplicates(nums):
    dc = {}
    for i in nums:
        if i not in dc:
            dc[i] = 1
        elif dc[i] == 2:
            left_over.append(i)
            pass
        else:
            dc[i] += 1
        total = []
    for k,v in dc.items():
        while v > 0:
            total.append(k)
            v -= 1
    nums = sorted(total)
    return len(nums)

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    remove_duplicates(nums)
