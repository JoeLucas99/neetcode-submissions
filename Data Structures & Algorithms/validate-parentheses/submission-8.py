class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {")" : "(", "}" : "{","]" : "[" }
        stack = []

        for c in s:
            if c in pMap:
                if stack and pMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

