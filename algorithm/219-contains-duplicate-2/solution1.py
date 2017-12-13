def contains_nearby_duplicate(nums, k):
    nums_dict = {}
    for i in range(len(nums)):
        index = nums_dict.get(nums[i])
        if index >=0 and i - index <= k:
            return True
        nums_dict[nums[i]] = i
    return False

if __name__ == '__main__':
    nums = [-1, -1]
    k = 1
    nums_dict = {}
    print contains_nearby_duplicate(nums, k)
