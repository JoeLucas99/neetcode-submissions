# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            curRight = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    curRight = node
                    q.append(node.left)
                    q.append(node.right)
            if curRight: 
                res.append(curRight.val)
        return res
        