# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Got through each list, check each point, compare, add, go, add entire last list to end
        dummy1 = ListNode()
        dummy = dummy1
        pnt1, pnt2 = list1, list2
        
        while pnt1 and pnt2:
            if pnt1.val < pnt2.val:
                dummy.next = pnt1
                pnt1 = pnt1.next
            else:
                dummy.next = pnt2
                pnt2 = pnt2.next
            dummy = dummy.next

        dummy.next = pnt1 or pnt2

        return dummy1.next           

        