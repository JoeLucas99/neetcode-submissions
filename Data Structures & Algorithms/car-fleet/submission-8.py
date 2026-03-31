class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = [(p, s) for p, s in zip(position, speed)]
        positions.sort(reverse = True)
        stack = []

        for p , s in positions:
            place = ((target - p) / s)
            stack.append(place)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
