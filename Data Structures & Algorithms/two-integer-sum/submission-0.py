class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setMap = {}

        for i, num in enumerate(nums):
            if target-num in setMap:
                return [setMap[target-num],i]
            else:
                setMap[num] = i

        
        