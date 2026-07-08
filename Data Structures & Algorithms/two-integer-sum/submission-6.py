class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numSet = {}

        for idx,num in enumerate(nums):
            if (target - num) in numSet:
                return [numSet[target-num],idx]
            
            numSet[num] = idx
        