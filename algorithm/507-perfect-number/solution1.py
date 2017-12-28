def check_perfect_numer(num):
    if num <=1 or num > 100000000:
            return False
    nums = [1]
    for i in range(2, num/2+1):
        if num % i == 0 and i not in nums:
            nums.append(i)
            nums.append(num/i)
    print nums
    if sum(nums) == num:
        return True
    return False

if __name__ == '__main__':
    num = 28
    print check_perfect_numer(num)