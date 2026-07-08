class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}

        for idx,num in enumerate(nums):
            if target-num in num_set:
                return [num_set[target-num],idx]
            else:
                num_set[num] = idx