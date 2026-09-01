# Last updated: 9/1/2026, 11:26:46 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k == 0:
9            return head
10
11        length = 1
12        tail = head
13
14        while tail.next:
15            tail = tail.next
16            length += 1
17
18        k %= length
19
20        if k == 0:
21            return head
22
23        new_tail = head
24
25        for _ in range(length - k - 1):
26            new_tail = new_tail.next
27
28        new_head = new_tail.next
29
30        new_tail.next = None
31        tail.next = head
32
33        return new_head