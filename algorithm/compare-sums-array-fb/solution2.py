def find_equal_sums(nums):
    # Edge cases
    if len(nums) == 0 or len(nums) == 1:
        print False
    if sum(nums) % 2 != 0:
        print False
    total = sum(nums) / 2
    current_total = 0
    for i in range(len(nums)):
        current_total += nums[i]
        if current_total == total:
            print nums[0:i+1]
            print nums[i+1:]
            return True
    print False
    return False

if __name__ == '__main__':
    nums = [1, 1, 1, 3, 8]
    find_equal_sums(nums)
