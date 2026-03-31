class Solution:
    def isValid(self, s: str) -> bool:
        parKey = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for c in s:
            if c in parKey:
                if stack and stack[-1] == parKey[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        