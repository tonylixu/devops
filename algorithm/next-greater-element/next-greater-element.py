def next_greater_element(nums1, nums2):
    re = []
    for i in nums1:
        index = nums2.index(i)
        find_it = 0
        if index == len(nums2) - 1:
           re.append(-1)
        else:
            for j in range(index+1, len(nums2)):
                if i < nums2[j]:
                    re.append(nums2[j])
                    find_it = 1
                    break
            if find_it == 0:
                re.append(-1)
    print re

if __name__ == '__main__':
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    next_greater_element(nums1, nums2)