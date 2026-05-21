# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        s1, s2 = "", ""
        while h1:
            s1 += str(h1.val)
            h1 = h1.next

        while h2:
            s2 += str(h2.val)
            h2 = h2.next
        
        r_s1, r_s2 = s1[::-1], s2[::-1]
        int1, int2 = int(r_s1), int(r_s2)
        int3 = int1 + int2
        s3 = str(int3)
        r_s3 = s3[::-1]

        dummy = ListNode()
        cur = dummy
        for i in range(len(s3)):
            cur.next = ListNode(val = int(r_s3[i]))
            cur = cur.next
        return dummy.next



        