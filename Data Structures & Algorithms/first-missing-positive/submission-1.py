class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        i = 0
        flag = True
        while flag:
            print(missing)
            if missing in nums:
                missing+=1
            else:
                flag = False
        
        return missing

        