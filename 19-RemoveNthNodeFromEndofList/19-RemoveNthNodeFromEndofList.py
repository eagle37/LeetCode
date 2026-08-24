# Last updated: 8/24/2026, 9:59:48 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        x = 0
9        temp = head
10        while temp:
11            x += 1
12            temp = temp.next
13        n = x - n
14        if n == 0:
15            return head.next
16        temp_ = head
17        for i in range(n-1):
18            temp_ = temp_.next
19        temp_.next = temp_.next.next
20        return head