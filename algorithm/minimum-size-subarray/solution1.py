def min_sub_array_len(s, nums):
    length = len(nums)
    min_len = length + 1
    min_array = []
    for i in range(length):
        for j in range(i+1, length+1):
            total = 0
            temp_array = []
            for k in range(i, j):
                total += nums[k]
                temp_array.append(nums[k])
            if total >= s and min_len > len(temp_array):
                min_len = len(temp_array)
                final_array = temp_array
    print final_array

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    min_sub_array_len(s, nums)