def largestNumber(nums):
    # Convert whole array of int to array of str
    # And sort the list
    nums_new = sorted([str(n) for n in nums], cmp=lambda a,b:-1 if a+b > b+a else 1)
    ret = ''.join(nums_new)
    if ret.startswith('0'):
        return '0'
    else:
        return ret

if __name__ == '__main__':
    #nums = [3, 30, 34, 5, 9]
    nums = [121, 12]
    print(largestNumber(nums))