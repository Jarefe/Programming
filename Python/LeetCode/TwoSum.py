
def twoSum(nums, target):

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            print([nums[i], nums[j]])
            if(nums[i] + nums[j] == target):
                return([i,j])

    
def twoSumCorrect(nums: List[int], target: int):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i,hashmap[complement]]
        # if no valid pair found, return empty list
        return []
