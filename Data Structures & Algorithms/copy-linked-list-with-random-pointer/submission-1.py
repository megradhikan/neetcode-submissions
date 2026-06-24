"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
    Creates a deep copy of a linked list with a random pointer using the
    O(1) space, one-pass approach.

    Args:
        head: The head of the original linked list.

    Returns:
        The head of the copied linked list.
    """
        # Edge case: if the list is empty, return None
        if not head:
            return None

        # Step 1: Interweave the new nodes into the original list.
        # The list will temporarily become O -> C -> O -> C...
        current = head
        while current:
            # Create a new node with the same value
            new_node = Node(current.val, current.next)
            # Weave the new node into the list
            current.next = new_node
            # Move to the next original node
            current = new_node.next

        # Step 2: Assign the random pointers for the new nodes.
        # The random pointer of the new node is the next of the original's random.
        current = head
        while current:
            # Check if the original node has a random pointer
            if current.random:
                # The new node is at current.next. Its random should point to the
                # new node corresponding to the original random node.
                # That new node is located at current.random.next.
                current.next.random = current.random.next
            # Move to the next original node in the interwoven list
            current = current.next.next

        # Step 3: Separate the original and new lists.
        # We will use two pointers, one for each list, to untangle them.
        original_head = head
        copied_head = head.next
        copied_current = copied_head

        while original_head:
            # Untangle the next pointers of the original list
            original_head.next = original_head.next.next

            # Untangle the next pointers of the copied list
            if copied_current.next:
                copied_current.next = copied_current.next.next

            # Move both pointers to their next respective nodes
            original_head = original_head.next
            copied_current = copied_current.next
            
        return copied_head