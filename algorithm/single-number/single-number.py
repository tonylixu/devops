def single_number(nums):
    re = 0
    for i in nums:
        re ^= i
    print re
    
if __name__ == '__main__':
    array = [1,2,2,3,3,4,4,5,5]
    single_number(array)
