class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1

        maxProfit = 0

        for r in range(len(prices)):
            currProfit = (prices[r] - prices[l])
            maxProfit = max(currProfit, maxProfit)
            if prices[r] < prices[l]:
                l = r
        return maxProfit