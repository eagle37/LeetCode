# Last updated: 9/20/2026, 7:36:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        scnd = slow.next
        slow.next = None

        prev = None
        while scnd:
            nex = scnd.next
            scnd.next = prev
            prev = scnd
            scnd = nex
        scnd = prev

        first = head
        while scnd:
            t1 = first.next
            t2 = scnd.next

            first.next = scnd
            scnd.next = t1
            first = t1
            scnd = t2

