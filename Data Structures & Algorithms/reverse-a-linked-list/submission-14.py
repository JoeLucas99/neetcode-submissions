# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prevNode = None

        while currNode:
            oldNode = currNode
            currNode = currNode.next
            oldNode.next = prevNode
            prevNode = oldNode
        return prevNode

