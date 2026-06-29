class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Each pile contain x bananas
        #We have h hours total to eat all the bananas
        #We cant eat more then 1 pile per hour
        #K is the eat rate
        l, r = 1, max(piles)
        min_eat_speed = r
        while l <= r:
            mid = l + (r - l) // 2
            cur_total_time = 0
            for pile in piles:
                cur_total_time += math.ceil(float(pile)/ mid)
            if cur_total_time <= h:
                min_eat_speed = min(min_eat_speed, mid)
                r = mid - 1
            else:
                l = mid + 1
        return min_eat_speed
