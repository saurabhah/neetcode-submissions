class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%= len(nums)
        
        nums.reverse()
        print(nums[:k])
        print(nums[k:])

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])