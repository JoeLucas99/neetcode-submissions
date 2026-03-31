class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        maxL, maxR = height[l], height[r]
        maxWater = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                maxWater += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxWater += maxR - height[r]
        return maxWater

        