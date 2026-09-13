# Last updated: 9/13/2026, 6:38:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        l = []
9        test = head
10        while test:
11            l.append(test.val)
12            test = test.next
13        return l == l[::-1]