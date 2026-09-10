# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        length, end = self.findLength(head)
        rotations = k % length
        if not rotations: return head
        partition = head
        for _ in range(length - rotations - 1):
            partition = partition.next
        res = partition.next
        partition.next = None
        end.next = head
        return res
        


    def findLength(self, node):
        length = 0
        prev = None
        while node:
            prev = node
            node = node.next
            length += 1
        return length, prev