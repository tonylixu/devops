def reshape_matrix(nums):
    new_nums = []
    new_nums2 = []
    r = 1
    c = 4
    for i in nums:
        new_nums += i
    if len(new_nums) < (r * c):
        print nums
    else:
        i = 0
        while i < r:
            row = []
            j = 0
            while j < c:
                row.append(new_nums.pop(0))
                j += 1
            #print row
            new_nums2.append(row)
            i += 1
        print new_nums2
                
if __name__=='__main__':
    nums = [
        [1, 2],
        [3, 4]
    ]
    reshape_matrix(nums)