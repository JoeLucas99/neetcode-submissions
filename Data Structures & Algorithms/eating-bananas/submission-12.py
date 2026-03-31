class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        minSpeed = max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            curHours = 0
            for p in piles:
                curHours += math.ceil(p / mid)
            if curHours <= h:
                minSpeed = mid
                r = mid - 1
            else:
                l = mid + 1
        return minSpeed
