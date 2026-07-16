# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            cur_level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    cur_level.append(cur.val)
            if cur_level:
                res.append(cur_level)
        return res