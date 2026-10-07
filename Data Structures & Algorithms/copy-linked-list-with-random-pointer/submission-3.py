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
        oldtonew={}
        cur=head
        while cur:
            oldtonew[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            oldtonew[cur].next=oldtonew.get(cur.next)
            oldtonew[cur].random=oldtonew.get(cur.random)
            cur=cur.next
        return oldtonew.get(head)
