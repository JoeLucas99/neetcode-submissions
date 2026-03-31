class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closingC = {'}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c in closingC:
                if stack and stack[-1] == closingC[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    