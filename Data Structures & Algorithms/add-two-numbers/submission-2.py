# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#Make dummy node, pointer, and carry, while l1/l2/carry, get vals if val else 0, add all, int div 10 for carry, 
#Mod 10 for val, make new node with val, iterate all, dmy.next = l1orl2 if nxt else None
#Return dmy.next
        dmyP = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1V = l1.val if l1 else 0
            l2V = l2.val if l2 else 0
            val = l1V + l2V + carry

            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            dmyP.next = newNode

            dmyP = dmyP.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        dmyP.next = l1 if l1 else None
        dmyP.next = l2 if l2 else None
        return dummy.next
        