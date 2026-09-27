# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp 
            temp = nxt
        first, second = head, prev
        res = 0
        while first and second:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next
        return res