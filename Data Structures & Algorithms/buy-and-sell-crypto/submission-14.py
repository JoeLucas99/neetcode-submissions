class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, maxP = float("inf"), float("-inf")
        for num in prices:
            small = min(small, num)
            if num - small > maxP:
                maxP = num - small
        return maxP    