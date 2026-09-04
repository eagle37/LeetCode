# Last updated: 9/4/2026, 4:32:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        while temp.next:
            a = temp.next
            if a.val == temp.val:
                temp.next = a.next
            else:
                temp = temp.next
        return head