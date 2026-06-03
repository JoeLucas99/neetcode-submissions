# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        #track prev node

        def dfs(root, maxSoFar):
            if not root: return 0
            res = 1 if root.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, root.val)
            res += dfs(root.left, maxSoFar)
            res += dfs(root.right, maxSoFar)
            return res
            
        
        return dfs(root, root.val)