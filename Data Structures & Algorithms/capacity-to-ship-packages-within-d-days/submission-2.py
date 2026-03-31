class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights) , sum(weights)
        res = r

        def canShip(weight):
            curWeight = weight
            daysPassed = 1

            for w in weights:
                if curWeight - w < 0:
                    daysPassed += 1
                    curWeight = weight
                curWeight -= w
            return daysPassed <= days

        while l <= r:
            mid_weight_guess = l + (r - l) // 2
            if canShip(mid_weight_guess):
                res = mid_weight_guess
                r = mid_weight_guess - 1
            else:
                l = mid_weight_guess + 1

        return res