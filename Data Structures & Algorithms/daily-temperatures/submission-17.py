class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_passed = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                indx, tmp = stack.pop()
                days_passed[indx] = (ind - indx)
            stack.append([ind, temp])
        return days_passed
        