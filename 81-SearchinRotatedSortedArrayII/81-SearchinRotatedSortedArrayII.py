# Last updated: 9/4/2026, 4:24:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        dummy = ListNode(0)
10        dummy.next = head
11
12        prev = dummy
13        curr = head
14
15        while curr and curr.next:
16
17            if curr.val == curr.next.val:
18                duplicate = curr.val
19
20                while curr and curr.val == duplicate:
21                    curr = curr.next
22
23                prev.next = curr
24
25            else:
26                prev = curr
27                curr = curr.next
28
29        return dummy.next