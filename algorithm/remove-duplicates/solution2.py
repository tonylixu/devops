def remove_duplicates(nums):
    if len(nums) <= 2: 
        print len(nums)
    p = 1
    c = 2
    while c < len(nums):
        if nums[c] == nums[p] and nums[c] == nums[p-1]:
            c += 1
        else:
            p += 1
            nums[p] = nums[c]
            c += 1
    print p + 1

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    remove_duplicates(nums)
