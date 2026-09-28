# Last updated: 9/29/2026, 12:15:05 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
8        while head and head.val == val:
9            head = head.next
10        if not head:
11            return head
12        temp = head
13        while temp.next:
14            if temp.next.val == val:
15                temp.next = temp.next.next
16            else:
17                temp = temp.next
18        return head