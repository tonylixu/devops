def find_kth_largest(nums, k):
    # We sort the array
    nums = sorted(nums)
    print nums[k*-1]

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    find_kth_largest(nums, k)