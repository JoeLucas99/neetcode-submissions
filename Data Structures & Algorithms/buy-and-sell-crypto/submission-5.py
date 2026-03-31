class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                currProf = (prices[r] - prices[l])
                mP = max(mP, currProf)
                r += 1
            
        return mP
            
            


        