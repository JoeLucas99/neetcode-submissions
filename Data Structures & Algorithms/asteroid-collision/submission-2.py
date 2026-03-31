class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
                continue
            ast_val = abs(ast) 
            exploded = False
            while stack and stack[-1] > 0:
                if stack[-1] < ast_val:
                    stack.pop()
                    continue
                elif stack[-1] == ast_val:
                    stack.pop()
                    exploded = True
                else: # stack[-1] > target_size
                    exploded = True
                break
            if not exploded:
                stack.append(ast)
        return stack