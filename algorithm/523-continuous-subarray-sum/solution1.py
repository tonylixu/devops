nums = [23, 2, 6, 4, 7]
k = 7

if not nums:
    print False
length = len(nums)
for i in range(length):
    for j in range(i+1, length):
        total = sum(nums[i:j+1])
        m = total % k if k else total
        if m == 0:
            print nums[i:j+1]
            print True
            break
print False
