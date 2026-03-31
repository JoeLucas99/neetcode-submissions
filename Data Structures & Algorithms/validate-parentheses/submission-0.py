class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ends = {')' : '(', '}': '{', ']' : '['}

        for c in s:
            if c in ends:
                if stack and ends[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        

        