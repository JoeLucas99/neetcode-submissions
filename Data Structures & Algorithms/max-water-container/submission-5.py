class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1
        maxWtr = 0
        while l < r:
            currHeight = min(heights[l], heights[r])
            currWater = currHeight * (r - l)
            maxWtr = max(maxWtr, currWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWtr