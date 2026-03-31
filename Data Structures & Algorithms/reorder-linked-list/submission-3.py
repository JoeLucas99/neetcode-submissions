# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find mid and end
        #Reverse Second half
        #Combine back and forth, return new head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secStart = slow.next
        slow.next, prev = None, None
        while secStart:
            tmp = secStart.next
            secStart.next = prev
            prev = secStart
            secStart = tmp
        
        p1, p2 = head, prev
        while p1 and p2:
            t1, t2 = p1.next, p2.next
            p1.next = p2
            p2.next = t1
            p1, p2 = t1, t2
        
        

        