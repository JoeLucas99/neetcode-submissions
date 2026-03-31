class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, maxP = float("inf"), 0
        for num in prices:
            small = min(small, num)
            if num - small > maxP:
                maxP = num - small
        return maxP    