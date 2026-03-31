class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(a + b)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b - a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(a * b)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b / a)
            else:
                stack.append(c)
        return int(stack[-1])

        