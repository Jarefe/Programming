def removeDuplicates(nums) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)



