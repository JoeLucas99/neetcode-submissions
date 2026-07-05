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
        copies = {None:None}
        cur = head
        while cur:
            copy_node = Node(cur.val)
            copies[cur] = copy_node
            cur = cur.next
        
        cur = head
        while cur:
            copy_node = copies[cur]
            copy_node.next = copies[cur.next]
            copy_node.random = copies[cur.random]
            cur = cur.next
        return copies[head]
