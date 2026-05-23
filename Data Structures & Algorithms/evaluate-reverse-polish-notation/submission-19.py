class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif tok == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif tok == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif tok == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(tok))
        return stack[-1]
        