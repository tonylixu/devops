nums = [1, 2, 3]
length = len(nums)
power_set = [[]]
for num in sorted(nums):
    power_set += [item + [num] for item in power_set]
print power_set