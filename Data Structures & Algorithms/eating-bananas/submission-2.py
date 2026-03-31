class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)
        minBanEatRate = r

        while l <= r:
            mid = l + (r - l) // 2
            timeToEat = 0
            for pile in piles:
                timeToEat += math.ceil(float(pile) / mid)
            if timeToEat <= h:
                minBanEatRate = mid
                r = mid - 1
            else:
                l = mid + 1
        return minBanEatRate
