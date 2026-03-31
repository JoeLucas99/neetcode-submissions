class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        minBanEatRate = r

        while l <= r:
            midRate = l + (r - l) // 2
            bansEaten = 0
            for pile in piles:
                bansEaten += math.ceil(float(pile)/ midRate)
            if bansEaten <= h:
                minBanEatRate = midRate
                r = midRate - 1
            else:
                l = midRate + 1
        return minBanEatRate

        