def largestNumber(nums):
    # Convert whole array of int to array of str
    nums_new = sorted([str(n) for n in nums], cmp=compare)
    ret = ''.join(nums_new)
    if ret.startswith('0'):
        return '0'
    else:
        return ret

def compare( a, b):
    return -1 if a+b > b+a else 1

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(largestNumber(nums))