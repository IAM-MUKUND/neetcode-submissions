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
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        curr = head
        dummy = Node(0)
        res = dummy
        while curr:
            res.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            res = res.next
        return dummy.next
                       