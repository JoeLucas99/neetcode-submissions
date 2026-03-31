"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#Make a hm, create copy nodes, store every copy in hm [cur:copy], go though again
#GEt copy, map its pointers, iterate, return hm[head]
        cur = head
        copyL = {None : None}

        while cur:
            copy = Node(cur.val)
            copyL[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copyL[cur]
            copy.next = copyL[cur.next]
            copy.random = copyL[cur.random]
            cur = cur.next
            
        return copyL[head]