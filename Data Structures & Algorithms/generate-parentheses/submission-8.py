class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def genPar(openN, closedN):
            if openN == n == closedN:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                genPar(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                genPar(openN, closedN + 1)
                stack.pop()
        genPar(0, 0)
        return res


        