# Last updated: 8/25/2026, 11:10:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        dummy = ListNode(0)
10        dummy.next = head
11
12        prev = dummy
13
14        while prev.next and prev.next.next:
15
16            first = prev.next
17            second = first.next
18
19            first.next = second.next
20            second.next = first
21            prev.next = second
22
23            prev = first
24
25        return dummy.next 