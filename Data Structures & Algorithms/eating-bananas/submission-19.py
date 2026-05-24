class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minEatRate = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            curEatRate = l + (r - l) // 2
            curTime = 0
            for p in piles:
                curTime += math.ceil(float(p) / curEatRate)
            if curTime <= h:
                minEatRate = min(curEatRate, minEatRate)
                r = curEatRate - 1
            else:
                l = curEatRate + 1
        return minEatRate
