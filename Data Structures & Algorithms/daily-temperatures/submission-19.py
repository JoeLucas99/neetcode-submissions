class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                dayInd, dayTemp = stack.pop()
                res[dayInd] = day - dayInd
            stack.append([day, temp])
        return res
        