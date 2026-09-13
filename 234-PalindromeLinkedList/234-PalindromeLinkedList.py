# Last updated: 9/13/2026, 7:08:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        test = head
        while test:
            l.append(test.val)
            test = test.next
        return l == l[::-1]