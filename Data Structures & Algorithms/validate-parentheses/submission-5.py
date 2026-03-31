class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedP = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closedP:
                if stack and closedP[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        