class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for s in operations:
            if s == "+":
                a = int(stack[-1])
                b = int(stack[-2])
                stack.append(str(a + b))
            elif s == "D":
                a = int(stack[-1])
                stack.append(str(a * 2))
            elif s == "C":
                stack.pop()
            else:
                stack.append(s)
        while stack:
            res += int(stack.pop())
        return res
        