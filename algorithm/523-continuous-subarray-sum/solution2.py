def check_sub_array_sum(nums, k):
    # Key is reminder, value is index
    dmap = {0:-1}
    total = 0
    for index,value in enumerate(nums):
        total += value
        m = total % k if k else total
        if m not in dmap:
            dmap[m] = index
        elif dmap[m] + 1 < index:
            return True
    return False

if __name__ == '__main__':
    nums = [0]
    k = 0
    print check_sub_array_sum(nums, k)