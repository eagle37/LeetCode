# Last updated: 9/29/2026, 12:19:26 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        node = None
9
10        while head:
11            temp = head.next
12            head.next = node
13            node = head
14            head = temp
15        
16        return node