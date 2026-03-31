class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = 0

        while l <= r:
            mid = l + (r - l) // 2
            possEaten = 0
            for pile in piles:
                possEaten += math.ceil(float(pile) / mid)
            if possEaten <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        