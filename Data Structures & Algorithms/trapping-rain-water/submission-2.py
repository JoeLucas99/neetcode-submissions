class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0 , len(height) - 1
        lM, rM = height[l], height[r]
        res = 0
        while l < r:
            if lM < rM:
                l += 1
                lM = max(height[l], lM)
                res += lM - height[l]
            else:
                r -= 1
                rM = max(height[r], rM)
                res += rM - height[r]
        return res
            
         