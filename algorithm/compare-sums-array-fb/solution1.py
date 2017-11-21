def find_equal_sums(nums):
    # Edge cases
    if len(nums) == 0 or len(nums) == 1:
        print False
    for i in range(len(nums)):
        if sum(nums[0:i+1]) == sum(nums[i+1:]):
            print nums[0:i+1]
            print nums[i+1:]
            return True
    print False
    return False

if __name__ == '__main__':
    nums = [1, 1, 1, 3]
    find_equal_sums(nums)