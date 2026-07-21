class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = CurrSum = 0
        prefix_sum = {0:1}

        for num in nums:
            CurrSum += num
            diff = CurrSum - k
            
            res += prefix_sum.get(diff,0)
            prefix_sum[CurrSum] = 1 + prefix_sum.get(CurrSum, 0)

        return res

        