# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, end = head, head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        second = mid.next
        prev = mid.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2

