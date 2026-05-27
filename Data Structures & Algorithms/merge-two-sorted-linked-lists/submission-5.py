# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        dummy = ListNode()
        dP = dummy

        while list1 and list2:
            #v1, v2 = list1.val(), list2.val()
            if list1.val <= list2.val:
                dP.next = list1
                list1 = list1.next
            else:
                dP.next = list2
                list2 = list2.next
            dP = dP.next
        
        if list1: dP.next = list1
        if list2: dP.next = list2

        return dummy.next
        


        