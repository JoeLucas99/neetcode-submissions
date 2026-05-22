class Solution:
    def maxArea(self, heights: List[int]):
        l, r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            curWater = (r - l) * min(heights[l], heights[r])
            maxWater = max(maxWater, curWater)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1

        return maxWater