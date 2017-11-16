def min_sub_array_len(s, nums):
    length = len(nums)
    if length == 0:
        print 0
    min_len = 10000
    pre_sum = [0] * length
    pre_sum[0] = nums[0]
    for i in range(1, length):
        pre_sum[i] = pre_sum[i-1] + nums[i]
    for i in range(length):
        total = 0
        for j in range(i, length):
            total = pre_sum[j] - pre_sum[i] + nums[i]
            if total >= s:
                min_len = min(min_len, (j-i+1))
    print min_len if min_len != 10000 else 0

if __name__ == '__main__':
    nums = [1, 1]
    s =  3 
    min_sub_array_len(s, nums)
