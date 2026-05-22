class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            if x == "+":
                b, a = stack.pop(), stack.pop()
                c = (int(a) + int(b))
                stack.append(a)
                stack.append(b)
                stack.append(str(c))
            elif x == "D":
                b = stack.pop()
                c = (2 * int(b))
                stack.append(b)
                stack.append(str(c))
            elif x == "C":
                stack.pop()
            else:
                stack.append(x)

        score = 0
        while stack:
            x = int(stack.pop())
            score += x
        return score

        