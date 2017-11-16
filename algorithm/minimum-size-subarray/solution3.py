def min_sub_array_len(s, nums):
    length = len(nums)
    if length == 0:
        return 0
    min_len = 100000
    total = 0
    pointer = 0;
    for i in range(length):
        total += nums[i]
        while total >= s:
            min_len = min(min_len, i-pointer+1)
            total -= nums[pointer]
            pointer += 1
    print min_len if min_len != 10000 else 0

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s =  7
    min_sub_array_len(s, nums)
