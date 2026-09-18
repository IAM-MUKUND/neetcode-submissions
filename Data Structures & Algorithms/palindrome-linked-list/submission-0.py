# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head.next
        slow = head
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
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True