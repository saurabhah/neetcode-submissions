class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        result = []
        word_count = Counter(nums)
        
     

        for key,value in word_count.items():
            if value > (len(nums) // 3):
                result.append(key)
        
        return result