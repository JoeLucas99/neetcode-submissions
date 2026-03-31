# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#Make dummyN and pointer, while l1,l2,and carry, get vals (if l1/l2 else 0), compute new val, compute carry
#Make new node for val, iterate (if l1/l2 else None), return dummy.next
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0

            curVal = l1v + l2v + carry
            carry = curVal // 10
            curVal = curVal % 10

            newNode = ListNode(curVal)
            cur.next = newNode

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        
        