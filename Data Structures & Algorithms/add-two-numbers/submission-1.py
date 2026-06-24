# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        cur=dummy
        while l1 or l2 or carry:
            if l1:
                v1=l1.val
                l1=l1.next
            else:
                v1=0
            if l2:
                v2=l2.val
                l2=l2.next
            else:
                v2=0
            s=v1+v2+carry
            carry=s//10
            s=s%10
            cur.next=ListNode(s)
            cur=cur.next
        return dummy.next
