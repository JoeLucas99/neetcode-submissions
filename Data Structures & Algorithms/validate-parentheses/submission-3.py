class Solution:
    def isValid(self, s: str) -> bool:
        closedParts = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in closedParts:
                if stack and closedParts[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        