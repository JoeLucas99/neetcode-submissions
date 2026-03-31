class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_key = { ")" : "(", "]" : "[", "}": "{"}

        for c in s:
            if c in par_key:
                if stack and par_key[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False