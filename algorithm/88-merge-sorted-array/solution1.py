def merge(nums1, m, nums2, n):
    tmp = [0 for i in range(m + n)]
    i = 0; j = 0; k = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            tmp[k] = nums1[i]; i += 1
        else:
            tmp[k] = nums2[j]; j += 1
        k += 1
    if i == m:
        while k < m + n:
            tmp[k] = nums2[j]; k += 1; j += 1
    else:
        while k < m + n:
            tmp[k] = nums1[i]; i += 1; k += 1
    for i in range(0, m + n):
        nums1[i] = tmp[i]

if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print nums1