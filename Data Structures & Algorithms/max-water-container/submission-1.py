class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left , right = 0, len(heights) -1

        max_len = 0

        while left <= right:

            min_len = min(heights[left] , heights[right])
            max_area = min_len * (right - left)
            max_len = max(max_len,max_area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_len 

        