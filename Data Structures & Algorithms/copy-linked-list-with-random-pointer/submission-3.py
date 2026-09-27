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
        nodehash = {None: None}
        curr = head
        while curr:
            nodehash[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = nodehash[curr]
            copy.next = nodehash[curr.next]
            copy.random = nodehash[curr.random]
            curr = curr.next
        return nodehash[head]
                       