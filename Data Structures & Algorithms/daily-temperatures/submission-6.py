class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        newChanges = [0] * (len(temperatures))

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, dayInd = stack.pop()
                newChanges[dayInd] = i - dayInd
            else:
                stack.append([temperatures[i], i])
        return newChanges
