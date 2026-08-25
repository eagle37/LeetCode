# Last updated: 8/25/2026, 11:03:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode(0)
            temp = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next

                temp = temp.next

            temp.next = l1 if l1 else l2

            return dummy.next

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])

            interval *= 2

        return lists[0]