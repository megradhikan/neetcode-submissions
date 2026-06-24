# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list using fast and slow pointers.
        # The slow pointer will stop at the end of the first half.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list.
        # First, detach the two halves.
        second_half_head = slow.next
        slow.next = None

        # Now, reverse the second half.
        prev = None
        curr = second_half_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # After reversal, 'prev' is the new head of the reversed second half.
        second_half_head_reversed = prev

        # Step 3: Merge the two halves alternately.
        # The first half starts at 'head', the second at 'second_half_head_reversed'.
        first_half_curr = head
        second_half_curr = second_half_head_reversed
        
        while second_half_curr:
            temp1 = first_half_curr.next
            temp2 = second_half_curr.next

            first_half_curr.next = second_half_curr
            second_half_curr.next = temp1

            first_half_curr = temp1
            second_half_curr = temp2