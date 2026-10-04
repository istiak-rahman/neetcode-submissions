class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        n = len(heights)
        left, right = 0, n - 1

        while left < right:
            amtWater = (right - left)*min(heights[right], heights[left])
            maxWater = max(maxWater, amtWater)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1
        
        return maxWater
