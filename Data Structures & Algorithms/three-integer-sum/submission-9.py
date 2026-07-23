class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and num == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
              
                totalSum = num + nums[l] + nums[r]
                if totalSum > 0:
                    r-=1
                elif totalSum < 0:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] ==  nums[l-1] and l < r:
                        l+=1
        
        return res
           
        
        
        
                






        
                

        