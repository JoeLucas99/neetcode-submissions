# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Split it, reverse second half, combine one by one
        cur, halfP = head, head
        while cur and cur.next:
            cur = cur.next.next
            halfP = halfP.next
        #Cur should be at end and halfP should be one before middle
        h2 = halfP.next
        halfP.next = None
        prev2 = None
        while h2:
            tmp = h2.next
            h2.next = prev2
            prev2 = h2
            h2 = tmp
        
        h1P, h2P = head, prev2
        while h2P:
            tmp1, tmp2 = h1P.next, h2P.next
            h1P.next = h2P
            h2P.next = tmp1
            h1P, h2P = tmp1, tmp2
        



        