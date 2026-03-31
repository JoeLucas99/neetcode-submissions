# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Find the height of each branch and then combine the two. Push that up and compare
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def depth(root):
            nonlocal diameter
            if not root:
                return 0
            left_H = depth(root.left)
            right_H = depth(root.right)
            diameter = max(diameter, left_H + right_H)
            return 1 + max(left_H, right_H)
        
        depth(root)
        return diameter
        