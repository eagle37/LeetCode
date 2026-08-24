# Last updated: 8/24/2026, 10:16:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = 0
        temp = head
        while temp:
            x += 1
            temp = temp.next
        n = x - n
        if n == 0:
            return head.next
        temp_ = head
        for i in range(n-1):
            temp_ = temp_.next
        temp_.next = temp_.next.next
        return head