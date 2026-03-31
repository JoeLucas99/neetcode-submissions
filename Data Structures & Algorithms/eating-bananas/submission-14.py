class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minEatRate = float("inf")
        while l <= r:
            midEatRate = l + (r - l) // 2
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile / midEatRate)
            if hoursTaken <= h:
                minEatRate = min(minEatRate, midEatRate)
                r = midEatRate - 1
            else:
                l = midEatRate + 1
        return minEatRate        