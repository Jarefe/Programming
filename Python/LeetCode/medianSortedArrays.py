def findMedianSortedArrays(nums1, nums2):
    sorted = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        val1 = nums1[i]
        val2 = nums2[j]

        # Add smaller value to sorted array first
        if val1 < val2:
            sorted.append(val1)
            i += 1
        else:
            sorted.append(val2)
            j += 1

    # .extend adds specified list elements (or any iterable) to end of current list        

    # Check for remaining elements in first array
    sorted.extend(nums1[i:])

    # Check for remaining elements in second array
    sorted.extend(nums2[j:])

    n = len(sorted)

    if n % 2 == 1:
        return sorted[n // 2] # use // for list indeces because // is floor division
    else:
        return (sorted[n // 2 - 1] + sorted[n // 2]) / 2


print(findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10,11,12,13,14,15,16,17]))