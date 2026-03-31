class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        maxWater = 0
        lMax, rMax = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                lMax = max(lMax, height[l])
                maxWater += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                maxWater += rMax - height[r]
        return maxWater


