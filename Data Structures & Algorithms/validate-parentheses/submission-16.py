class Solution:
    def isValid(self, s: str) -> bool:
        parentKey = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        
        for c in s:
            if c in parentKey:
                if stack and stack[-1] == parentKey[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 
        return True if not stack else False