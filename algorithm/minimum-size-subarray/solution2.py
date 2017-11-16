def min_sub_array_len(s, nums):
    length = len(nums)
    min_len = length + 1
    pre_sum = [0] * length
    pre_sum[0] = nums[0]
    for i in range(length):
        pre_sum[i] = pre_sum[i-1] + nums[i]
    for i in range(length):
        total = 0
        for j in range(i, length):
            total = pre_sum[j] - pre_sum[i] + nums[i]
        if total >= s:
            min_len = min(min_len, (j-i+1))
    print min_len
            


if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    min_sub_array_len(s, nums)