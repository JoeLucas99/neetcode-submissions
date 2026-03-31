# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        lP = dummy
        rP = head

        while n > 0:
            rP = rP.next
            n -= 1
        
        while rP:
            rP = rP.next
            lP = lP.next
        
        lP.next = lP.next.next

        return dummy.next
