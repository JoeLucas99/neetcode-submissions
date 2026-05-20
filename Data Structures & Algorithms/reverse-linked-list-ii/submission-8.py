# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #Left isnt garaunteed to be head, but it could be
    #Should check if head = left, if so right will be new head, if not return from head
    #Use while loops to count down
    #Get to left, then run the switch loop until right, but put a pointer on right + 1 first to make the
    # first prev point to it

        leftC, rightC = left, right
        dummy = ListNode(next = head)
        leftP, preLP, rightP = dummy, dummy, dummy

        for i in range(leftC - 1):
            preLP = preLP.next
        leftP = preLP.next

        for i in range(rightC):
            rightP = rightP.next

        afterRightP = rightP.next
        prev = afterRightP

        for i in range(rightC - leftC + 1):
            tmp = leftP.next
            leftP.next = prev
            prev = leftP
            leftP = tmp
        preLP.next = prev
        return dummy.next

