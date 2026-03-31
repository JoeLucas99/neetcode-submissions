class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsP = [(p, s) for p, s in zip(position, speed)]
        carsP.sort(reverse = True)
        stack = []

        for p, s in carsP:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        
        return len(stack)