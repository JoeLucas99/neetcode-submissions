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
        cur = head
        copyList = {None : None}
        while cur:
            copyNode = Node(x = cur.val)
            copyList[cur] = copyNode
            cur = cur.next
        cur = head
        while cur:
            copyNode = copyList[cur]
            copyNode.next = copyList[cur.next]
            copyNode.random = copyList[cur.random]
            cur = cur.next
        return copyList[head]
        