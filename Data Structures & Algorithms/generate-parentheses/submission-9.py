class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def parent(openN, closedN):
            if openN == n == closedN:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                parent(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                parent(openN, closedN+1)
                stack.pop()
        parent(0, 0)
        return res
        